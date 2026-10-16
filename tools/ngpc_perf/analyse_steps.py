#!/usr/bin/env python3
"""Compare actual gameplay updates in MAME frame/step CSV captures.

Input CSV columns: frame,port_steps (one row per displayed frame).
'port_steps' is a monotonically increasing gameplay-update counter during
an individual capture; repeated values indicate no simulation update.

A counter reset/wrap needs a fresh capture or preprocessing: this tool ignores
negative changes by default. No ROMs, sprites, external dependencies, or
proprietary tools are required.
"""
from __future__ import annotations

import argparse
from collections import Counter
import csv
import json
from pathlib import Path


def load_trace(path):
    """Return (frame, port_steps) in capture order; validate clean input."""
    rows = []
    with Path(path).open(newline='', encoding='utf-8-sig') as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames or not {'frame', 'port_steps'} <= set(reader.fieldnames):
            raise ValueError(f'{path}: expected CSV headers frame,port_steps')
        for line_no, row in enumerate(reader, start=2):
            try:
                frame = int(row['frame'])
                steps = int(row['port_steps'])
            except (TypeError, ValueError) as ex:
                raise ValueError(f'{path}:{line_no}: invalid integer') from ex
            if rows and frame != rows[-1][0] + 1:
                raise ValueError(f'{path}:{line_no}: expected consecutive display frames')
            if rows and steps < rows[-1][1]:
                raise ValueError(f'{path}:{line_no}: step counter decreased; split capture or unwrap')
            rows.append((frame,steps))
    if len(rows) < 2:
        raise ValueError(f'{path}: need at least two display frames')
    return rows


def analyse(rows, start, end, threshold=7, display_hz=60):
    """Count changes from actual steps, with start inclusive/end exclusive.

    Intervals are measured between consecutive change frames. An interval is
    included if its *first* change frame occurs in [start,end); enough capture
    beyond end is needed to include the final interval accurately.
    """
    if end <= start or threshold < 0 or display_hz <= 0:
        raise ValueError('end must exceed start; threshold nonnegative; Hz positive')
    if rows[0][0] > start-1 or rows[-1][0] <= end:
        raise ValueError('capture must include one frame before start and frames after end')
    changes = [f for (f,n),(prev,p) in zip(rows[1:],rows[:-1]) if n > p]
    gaps = [b-a for a,b in zip(changes,changes[1:]) if start <= a < end]
    if not gaps:
        raise ValueError('no complete gameplay intervals found in window')
    total = end-start
    histogram = dict(sorted(Counter(gaps).items()))
    return {
        'window_display_frames':[start,end],
        'display_hz':display_hz,
        'window_seconds':round(total/display_hz,6),
        'logic_intervals':len(gaps),
        'mean_logic_intervals_per_second':round(len(gaps)*display_hz/total,3),
        'worst_logic_gap_display_frames':max(gaps),
        'gaps_above_threshold':sum(g > threshold for g in gaps),
        'stall_threshold_display_frames':threshold,
        'interval_histogram':{str(k):v for k,v in histogram.items()},
    }


def compare(old,new):
    if old['window_display_frames'] != new['window_display_frames']:
        raise ValueError('captures use different windows')
    return {
        'baseline':old, 'candidate':new,
        'change':{
            'logic_intervals':new['logic_intervals']-old['logic_intervals'],
            'worst_gap':new['worst_logic_gap_display_frames']-old['worst_logic_gap_display_frames'],
            'stalls_above_threshold':new['gaps_above_threshold']-old['gaps_above_threshold'],
        }
    }


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline',type=Path,required=True)
    parser.add_argument('--candidate',type=Path,required=True)
    parser.add_argument('--start',type=int,required=True)
    parser.add_argument('--end',type=int,required=True)
    parser.add_argument('--threshold',type=int,default=7)
    parser.add_argument('--hz',type=int,default=60)
    parser.add_argument('--json',action='store_true',help='machine-readable report')
    args=parser.parse_args(argv)
    report=compare(analyse(load_trace(args.baseline),args.start,args.end,args.threshold,args.hz),
                   analyse(load_trace(args.candidate),args.start,args.end,args.threshold,args.hz))
    if args.json:
        print(json.dumps(report,indent=2))
    else:
        print(f"Window {args.start}..{args.end} frames at {args.hz} Hz")
        for label in ('baseline','candidate'):
            r=report[label]
            print(f"{label.title():9} updates={r['logic_intervals']:4} "
                  f"worst_gap={r['worst_logic_gap_display_frames']:2} "
                  f"long_gaps={r['gaps_above_threshold']:3} "
                  f"rate={r['mean_logic_intervals_per_second']:.2f}/s")
        print('Changes:',report['change'])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

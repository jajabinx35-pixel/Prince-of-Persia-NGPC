"""Unit tests require only Python 3.9+ standard library."""
import sys
import tempfile
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from analyse_steps import analyse, compare, load_trace


class AnalyseStepsTest(unittest.TestCase):
    def test_known_intervals(self):
        rows=[(i,sum(1 for n in (2,7,12,16,22,28) if n<=i)) for i in range(0,31)]
        stats=analyse(rows,2,25,threshold=5)
        self.assertEqual(stats['logic_intervals'],5)
        self.assertEqual(stats['worst_logic_gap_display_frames'],6)
        self.assertEqual(stats['gaps_above_threshold'],2)
        self.assertEqual(stats['interval_histogram'],{'4':1,'5':2,'6':2})

    def test_unchanged_not_counted(self):
        rows=[(i,0 if i<4 else 1 if i<9 else 2) for i in range(0,13)]
        stats=analyse(rows,2,10)
        self.assertEqual(stats['logic_intervals'],1)
        self.assertEqual(stats['worst_logic_gap_display_frames'],5)

    def test_window_must_have_context(self):
        with self.assertRaises(ValueError):
            analyse([(i,i) for i in range(1,12)],1,10)

    def test_nonconsecutive_frame_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            file=Path(d)/'steps.csv'
            file.write_text('frame,port_steps\n1,1\n3,2\n')
            with self.assertRaisesRegex(ValueError,'consecutive'):
                load_trace(file)

    def test_counter_decrease_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            file=Path(d)/'steps.csv'
            file.write_text('frame,port_steps\n1,10\n2,9\n')
            with self.assertRaisesRegex(ValueError,'decreased'):
                load_trace(file)

    def test_compare(self):
        rows=[(i,sum(1 for n in (2,7,12,17,22,27) if n<=i)) for i in range(0,31)]
        a=analyse(rows,2,24)
        c=analyse(rows,2,24)
        self.assertEqual(compare(a,c)['change']['logic_intervals'],0)

    def test_included_leap67_data(self):
        samples=ROOT/'samples'
        old=analyse(load_trace(samples/'leap66_level5_steps.csv'),5700,7500)
        new=analyse(load_trace(samples/'leap67_level5_steps.csv'),5700,7500)
        self.assertEqual((old['logic_intervals'],old['worst_logic_gap_display_frames'],old['gaps_above_threshold']), (264,13,81))
        self.assertEqual((new['logic_intervals'],new['worst_logic_gap_display_frames'],new['gaps_above_threshold']), (360,5,0))

if __name__=='__main__':unittest.main()

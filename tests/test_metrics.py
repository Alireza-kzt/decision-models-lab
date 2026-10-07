import math
import unittest
from decision_lab.schema import Example
from decision_lab.metrics import compute_metrics
from test_schema import example

class MetricTests(unittest.TestCase):
    def setUp(self):
        self.ex=[Example.from_dict(example("1","a",group="1")),Example.from_dict(example("2","b",group="2"))]
    def test_perfect(self):
        m=compute_metrics(self.ex,{"1":{"a":1,"b":0},"2":{"a":0,"b":1}})
        for key in ("accuracy","macro_f1","coverage"): self.assertEqual(m[key],1)
        for key in ("nll","brier_multiclass_sum","ece_top_label","selective_risk"): self.assertEqual(m[key],0)
    def test_uniform_hand_calculation(self):
        m=compute_metrics(self.ex,{"1":{"a":.5,"b":.5},"2":{"a":.5,"b":.5}})
        self.assertEqual(m["accuracy"],.5);self.assertAlmostEqual(m["macro_f1"],1/3)
        self.assertAlmostEqual(m["nll"],math.log(2));self.assertEqual(m["brier_multiclass_sum"],.5)
        self.assertEqual(m["coverage"],0);self.assertIsNone(m["selective_risk"])
    def test_ece_and_selection(self):
        m=compute_metrics(self.ex,{"1":{"a":.8,"b":.2},"2":{"a":.8,"b":.2}})
        self.assertAlmostEqual(m["ece_top_label"],.3);self.assertEqual(m["selective_risk"],.5)
    def test_canonical_ties(self):
        self.ex[0].options.clear();self.ex[0].options.update({"b":"Second","a":"First"})
        m=compute_metrics(self.ex,{"1":{"b":.5,"a":.5},"2":{"a":.5,"b":.5}})
        self.assertEqual(m["accuracy"],.5)
    def test_zero_probability_clipped(self):
        m=compute_metrics(self.ex,{"1":{"a":0,"b":1},"2":{"a":1,"b":0}})
        self.assertTrue(math.isfinite(m["nll"]));self.assertAlmostEqual(m["nll"],-math.log(1e-15))
        self.assertEqual(m["brier_multiclass_sum"],2)
    def test_invalid_parameters(self):
        p={"1":{"a":.5,"b":.5},"2":{"a":.5,"b":.5}}
        for opts in [{"bins":0},{"bins":True},{"threshold":float("nan")},{"threshold":2}]:
            with self.subTest(opts=opts),self.assertRaises(ValueError): compute_metrics(self.ex,p,**opts)
    def test_empty_input(self):
        with self.assertRaises(ValueError): compute_metrics([], {})

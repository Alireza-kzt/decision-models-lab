import json
from pathlib import Path
import tempfile
import unittest
from decision_lab.schema import Example, load_examples, load_predictions, read_jsonl, validate_probabilities

def example(ident="1", label="a", split="test", group="g"):
    return {"id":ident,"state":"original test input","question":"Pick a label", "options":{"a":"First","b":"Second"},"label":label,"group_id":group,"split":split}

class SchemaTests(unittest.TestCase):
    def temp_jsonl(self, rows):
        folder = tempfile.TemporaryDirectory(); self.addCleanup(folder.cleanup)
        path = Path(folder.name)/"data.jsonl"
        path.write_text("\n".join(json.dumps(r) for r in rows),encoding="utf-8")
        return path
    def test_valid_example(self):
        self.assertEqual(Example.from_dict(example()).label,"a")
    def test_bad_label(self):
        with self.assertRaises(ValueError): Example.from_dict(example(label="c"))
    def test_group_leakage(self):
        path=self.temp_jsonl([example(),example("2",split="train")])
        with self.assertRaises(ValueError): load_examples(path)
    def test_duplicate_id(self):
        with self.assertRaises(ValueError): load_examples(self.temp_jsonl([example(),example()]))
    def test_mixed_eval_split(self):
        with self.assertRaises(ValueError): load_examples(self.temp_jsonl([example(),example("2",split="dev",group="other")]),evaluation=True)
    def test_variable_options_rejected(self):
        row=example("2",group="other"); row["options"]["c"]="Third"
        with self.assertRaises(ValueError): load_examples(self.temp_jsonl([example(),row]),evaluation=True)
    def test_probability_failures(self):
        cases=[{"a":float("nan"),"b":1.0},{"a":float("inf"),"b":0.0},{"a":True,"b":0}, {"a":.8,"b":.8},{"a":-0.1,"b":1.1},{"a":1.0},{"a":"0.5","b":.5}]
        for case in cases:
            with self.subTest(case=case), self.assertRaises(ValueError): validate_probabilities(case,{"a","b"})
    def test_no_renormalization(self):
        p=validate_probabilities({"a":.2,"b":.8},{"a","b"}); self.assertEqual(p["a"],.2)
    def test_prediction_id_join(self):
        ex=[Example.from_dict(example()),Example.from_dict(example("2",label="b",group="g2"))]
        path=self.temp_jsonl([{"id":"2","probabilities":{"a":.1,"b":.9}},{"id":"1","probabilities":{"a":.8,"b":.2}}])
        self.assertEqual(load_predictions(path,ex)["1"]["a"],.8)
    def test_missing_prediction(self):
        ex=[Example.from_dict(example()),Example.from_dict(example("2",group="g2"))]
        with self.assertRaises(ValueError): load_predictions(self.temp_jsonl([{"id":"1","probabilities":{"a":1,"b":0}}]),ex)
    def test_unknown_prediction(self):
        with self.assertRaises(ValueError): load_predictions(self.temp_jsonl([{"id":"other","probabilities":{"a":1,"b":0}}]),[Example.from_dict(example())])
    def test_empty_jsonl(self):
        with self.assertRaises(ValueError): read_jsonl(self.temp_jsonl([]))
    def test_duplicate_json_keys(self):
        p=self.temp_jsonl([]); p.write_text('{"id":"1","id":"2"}',encoding="utf-8")
        with self.assertRaises(ValueError): read_jsonl(p)
    def test_nonfinite_state(self):
        row=example();row["state"]={"x":float("nan")}
        with self.assertRaises(ValueError): Example.from_dict(row)

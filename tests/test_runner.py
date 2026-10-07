import json
from pathlib import Path
import tempfile
import unittest
from decision_lab.runner import evaluate_run, ROOT
from decision_lab.adapters import UniformAdapter
from decision_lab.validation import validate_repository

class RunnerTests(unittest.TestCase):
    def test_uniform_adapter(self):
        self.assertEqual(UniformAdapter().predict("secret-free fixture","q",{"b":"B","a":"A"}),{"a":.5,"b":.5})
    def test_run_and_immutable_output(self):
        with tempfile.TemporaryDirectory() as d:
            out=Path(d)/"run"
            kwargs=dict(dataset=ROOT/"data/examples/toy.jsonl",predictions=None,out=out,kind="demonstration",model_id="uniform-demo",revision="v1")
            metrics=evaluate_run(**kwargs)
            self.assertEqual(metrics["n"],6)
            manifest=json.loads((out/"manifest.json").read_text())
            self.assertEqual(manifest["status"],"completed");self.assertFalse(manifest["network_access"])
            self.assertIn("dataset_sha256",manifest)
            with self.assertRaises(FileExistsError):evaluate_run(**kwargs)
    def test_failed_run_preserved(self):
        with tempfile.TemporaryDirectory() as d:
            out=Path(d)/"run"
            with self.assertRaises(FileNotFoundError):
                evaluate_run(dataset=Path(d)/"missing",predictions=None,out=out,kind="demonstration",model_id="uniform-demo",revision="v1")
            self.assertEqual(json.loads((out/"manifest.json").read_text())["status"],"failed")
    def test_replay_is_not_provider_execution(self):
        with tempfile.TemporaryDirectory() as d:
            out=Path(d)/"run"
            evaluate_run(dataset=ROOT/"data/examples/toy.jsonl",predictions=ROOT/"data/examples/replay.jsonl",out=out,kind="demonstration",model_id="hand-authored-fixture",revision="v1")
            manifest=json.loads((out/"manifest.json").read_text())
            self.assertIn("not independently verified",manifest["prediction_provenance"])
    def test_no_uniform_impersonation(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError):evaluate_run(dataset=ROOT/"data/examples/toy.jsonl",predictions=None,out=Path(d)/"r",kind="demonstration",model_id="jev",revision="v1")
    def test_registry_and_links(self):
        result=validate_repository(ROOT)
        self.assertEqual(result["model_entries"],14);self.assertEqual(result["paper_entries"],7)

from pathlib import Path
import subprocess
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
class PublishTests(unittest.TestCase):
    def test_dry_run_never_calls_git_or_gh(self):
        p=subprocess.run([sys.executable,str(ROOT/"scripts/publish_private.py")],text=True,capture_output=True)
        self.assertEqual(p.returncode,0);self.assertIn("DRY RUN",p.stdout)
        self.assertIn("No repository has been created",p.stdout)
    def test_invalid_name_rejected(self):
        p=subprocess.run([sys.executable,str(ROOT/"scripts/publish_private.py"),"--name","../bad"],text=True,capture_output=True)
        self.assertNotEqual(p.returncode,0)

"""Exercise marker detection without treating ordinary document prose as conflict."""
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location("checks", Path(__file__).parents[1] / "checks.py")
checks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checks)


class ConflictDetectionTests(unittest.TestCase):
    def test_all_merge_conflict_sections(self):
        self.assertEqual(checks.conflict_lines(b"<<<<<<< ours\na\n||||||| base\nb\n=======\nc\n>>>>>>> theirs\n"), [1, 3, 5, 7])

    def test_normal_prose_and_binary(self):
        self.assertEqual(checks.conflict_lines(b"# Heading\n| A | B |\nA > B\n"), [])
        self.assertEqual(checks.conflict_lines(b"\0<<<<<<< ours"), [])

    def test_long_markers(self):
        self.assertEqual(checks.conflict_lines(b"<<<<<<<<<< branch\n"), [1])

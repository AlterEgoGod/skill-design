"""Regression tests for strict contrast and packaged reference links. No dependencies."""
import json
from pathlib import Path
import re
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ContrastTests(unittest.TestCase):
    def check(self, fg, bg, required=None):
        command = [sys.executable, str(ROOT / 'scripts/check_design.py'), 'contrast',
                   '--foreground', fg, '--background', bg]
        if required:
            command += ['--require', required]
        return subprocess.run(command, capture_output=True, text=True)

    def test_information_mode_stays_compatible(self):
        r = self.check('#ffffff', '#ffffff')
        self.assertEqual(r.returncode, 0)
        self.assertEqual(json.loads(r.stdout)['ratio'], 1)

    def test_strict_fail_and_pass(self):
        for role in ['normal-text', 'large-text', 'non-text']:
            with self.subTest(role=role):
                self.assertEqual(self.check('#ffffff', '#ffffff', role).returncode, 1)
                self.assertEqual(self.check('#000000', '#ffffff', role).returncode, 0)

    def test_unrounded_threshold(self):
        self.assertEqual(self.check('#777777', '#ffffff', 'normal-text').returncode, 1)
        self.assertEqual(self.check('#767676', '#ffffff', 'normal-text').returncode, 0)
        self.assertEqual(self.check('#777777', '#ffffff', 'large-text').returncode, 0)

    def test_invalid_color(self):
        self.assertEqual(self.check('#fff', '#ffffff', 'normal-text').returncode, 2)


class PackageTests(unittest.TestCase):
    def test_markdown_file_links_exist(self):
        for file in ROOT.rglob('*.md'):
            for target in re.findall(r'\]\(([^)]+)\)', file.read_text(encoding='utf-8')):
                if '://' in target or target.startswith('#'):
                    continue
                with self.subTest(file=str(file), target=target):
                    self.assertTrue((file.parent / target.split('#')[0]).exists())


if __name__ == '__main__':
    unittest.main()

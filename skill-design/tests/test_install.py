from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]


class InstallTests(unittest.TestCase):
    def test_dry_run_and_preserved_instructions(self):
        with tempfile.TemporaryDirectory() as temp:
            p=Path(temp);f=p/'AGENTS.md';f.write_text('Existing instructions\n')
            cmd=[sys.executable,str(ROOT/'scripts/install_skill.py'),'--agent','codex','--project',temp,'--instructions']
            self.assertEqual(subprocess.run(cmd+['--dry-run'],capture_output=True).returncode,0)
            self.assertFalse((p/'.agents').exists())
            self.assertEqual(subprocess.run(cmd,capture_output=True).returncode,0)
            self.assertTrue((p/'.agents/skills/skill-design/SKILL.md').exists())
            self.assertTrue(f.read_text().startswith('Existing instructions'))
            self.assertEqual(f.read_text().count('<!-- skill-design:start -->'),1)
            before=f.read_bytes()
            self.assertEqual(subprocess.run(cmd,capture_output=True).returncode,2)
            self.assertEqual(f.read_bytes(),before)

    def test_claude_location(self):
        with tempfile.TemporaryDirectory() as temp:
            cmd=[sys.executable,str(ROOT/'scripts/install_skill.py'),'--agent','claude','--project',temp]
            self.assertEqual(subprocess.run(cmd,capture_output=True).returncode,0)
            self.assertTrue((Path(temp)/'.claude/skills/skill-design/SKILL.md').exists())


if __name__=='__main__':
    unittest.main()

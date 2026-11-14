"""Install this complete skill; instructions are opt-in, existing installations stay intact."""
import argparse
from pathlib import Path
import shutil

RULE = '''<!-- skill-design:start -->
For UI creation or modification, load the installed skill-design skill. Preserve the existing brand and component system. Verify affected states, keyboard use, contrast and responsiveness; fix introduced regressions and report only checks actually performed. Do not apply to backend-only work or redesign unrelated screens.
<!-- skill-design:end -->
'''


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--agent', choices=['codex', 'claude'], required=True)
    p.add_argument('--scope', choices=['project', 'user'], default='project')
    p.add_argument('--project', type=Path, default=Path.cwd())
    p.add_argument('--instructions', action='store_true')
    p.add_argument('--dry-run', action='store_true')
    a = p.parse_args()
    source = Path(__file__).resolve().parents[1]
    base = a.project.resolve() if a.scope == 'project' else Path.home()
    target = base / ('.agents' if a.agent == 'codex' else '.claude') / 'skills' / 'skill-design'
    if target.exists():
        p.error('Destination exists. Back up and update it explicitly; no files overwritten.')
    if a.instructions and a.scope != 'project':
        p.error('--instructions is project-only; global instructions are not changed')
    instructions = base / ('AGENTS.md' if a.agent == 'codex' else 'CLAUDE.md')
    text = instructions.read_text(encoding='utf-8') if a.instructions and instructions.exists() else ''
    if '<!-- skill-design:start -->' in text and '<!-- skill-design:end -->' not in text:
        p.error('Incomplete managed instructions block; inspect it manually')
    print('Install:', target)
    if a.instructions:
        print('Instructions:', instructions)
    if a.dry_run:
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, target, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    if a.instructions and '<!-- skill-design:start -->' not in text:
        instructions.write_text(text.rstrip() + '\n\n' + RULE, encoding='utf-8')
    print('Installed. Verify discovery in a new agent session.')


if __name__ == '__main__':
    main()

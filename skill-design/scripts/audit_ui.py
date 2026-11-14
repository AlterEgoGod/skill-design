"""Optional Playwright snapshot audit; no installs, app actions or external axe downloads."""
import argparse
import json
from pathlib import Path
import sys
from urllib.parse import urlparse


def width(value):
    try:
        n = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError('Width must be an integer') from exc
    if not 240 <= n <= 7680:
        raise argparse.ArgumentTypeError('Width must be between 240 and 7680')
    return n


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--url', required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--widths', nargs='+', type=width, default=[320, 768, 1440])
    parser.add_argument('--theme', choices=['light', 'dark', 'neutral'])
    parser.add_argument('--axe', type=Path)
    parser.add_argument('--executable')
    parser.add_argument('--strict', action='store_true')
    args = parser.parse_args()
    if urlparse(args.url).scheme not in ['http', 'https', 'file']:
        parser.error('Use http, https or file URL')
    if args.axe and not args.axe.is_file():
        parser.error('axe-core script does not exist')
    report = {'url': args.url, 'requested_theme': args.theme, 'checks': [], 'error': None,
              'limitations': ['Initial state only', 'No keyboard or task-flow verification',
                              'No full WCAG certification', 'Theme contract must match application']}
    try:
        from playwright.sync_api import sync_playwright
        args.output.mkdir(parents=True, exist_ok=True)
        with sync_playwright() as pw:
            options = {'headless': True}
            if args.executable:
                options['executable_path'] = args.executable
            browser = pw.chromium.launch(**options)
            try:
                for viewport in dict.fromkeys(args.widths):
                    page = browser.new_page(viewport={'width': viewport, 'height': 900},
                                            reduced_motion='reduce')
                    errors = []
                    page.on('pageerror', lambda err: errors.append(str(err)))
                    response = page.goto(args.url, wait_until='load', timeout=30000)
                    if response and response.status >= 400:
                        raise RuntimeError('HTTP ' + str(response.status))
                    if args.theme:
                        page.evaluate('''theme => {
                          document.documentElement.dataset.designTheme = theme;
                          document.documentElement.classList.toggle('dark', theme === 'dark');
                        }''', args.theme)
                    page.evaluate('() => document.fonts.ready')
                    metrics = page.evaluate('''() => ({
                      viewport: innerWidth, content: document.documentElement.scrollWidth,
                      theme: document.documentElement.dataset.designTheme || null,
                      darkClass: document.documentElement.classList.contains('dark')
                    })''')
                    axe = None
                    if args.axe:
                        page.add_script_tag(path=str(args.axe.resolve()))
                        axe = page.evaluate('''async () => {
                          const r = await axe.run(document);
                          return {violations:r.violations, incomplete:r.incomplete};
                        }''')
                    name = str(viewport) + '.png'
                    page.screenshot(path=str(args.output / name), full_page=True)
                    report['checks'].append({'width': viewport, 'metrics': metrics,
                        'horizontal_overflow': metrics['content'] > metrics['viewport'],
                        'page_errors': errors, 'axe': axe, 'screenshot': name})
                    page.close()
            finally:
                browser.close()
    except Exception as exc:
        report['error'] = str(exc)
    try:
        args.output.mkdir(parents=True, exist_ok=True)
        (args.output / 'report.json').write_text(json.dumps(report, ensure_ascii=True, indent=2), encoding='utf-8')
    except OSError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    print(json.dumps({'report': str(args.output / 'report.json'), 'completed': len(report['checks']),
                      'error': report['error']}))
    if report['error']:
        return 2
    failed = any(c['horizontal_overflow'] or c['page_errors'] or
                 (c['axe'] and c['axe']['violations']) for c in report['checks'])
    return 1 if args.strict and failed else 0


if __name__ == '__main__':
    sys.exit(main())

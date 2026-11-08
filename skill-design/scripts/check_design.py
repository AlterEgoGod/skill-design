"""Local contrast and font coverage checks. No network or mutations."""
import argparse
import json
import re
import sys

def color(value):
    if not re.fullmatch(r'#[0-9a-fA-F]{6}', value):
        raise argparse.ArgumentTypeError('Use opaque sRGB #RRGGBB')
    return value

def luminance(value):
    rgb=[int(value[i:i+2],16)/255 for i in (1,3,5)]
    rgb=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in rgb]
    return sum(v*w for v,w in zip(rgb,(.2126,.7152,.0722)))

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    commands=parser.add_subparsers(dest='command',required=True)
    contrast=commands.add_parser('contrast')
    contrast.add_argument('--foreground',type=color,required=True)
    contrast.add_argument('--background',type=color,required=True)
    font=commands.add_parser('font')
    font.add_argument('path')
    args=parser.parse_args()
    if args.command=='contrast':
        a,b=sorted([luminance(args.foreground),luminance(args.background)])
        ratio=(b+.05)/(a+.05)
        print(json.dumps({'ratio':ratio,'normal_text_AA':ratio>=4.5,'large_text_AA':ratio>=3,'non_text_threshold':ratio>=3}))
        return 0
    try:
        from fontTools.ttLib import TTFont
    except ImportError:
        print('Font inspection requires FontTools; WOFF2 also requires Brotli.',file=sys.stderr)
        return 2
    groups={'EN':'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','RU':'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя','symbols':'0123456789₽$€—№'}
    try:
        with TTFont(args.path) as data:
            cmap=data.getBestCmap() or {}
            result={'family':data['name'].getDebugName(1),'version':data['name'].getDebugName(5),'groups':{k:{'supported':sum(ord(c) in cmap for c in chars),'total':len(chars),'missing':[c for c in chars if ord(c) not in cmap]} for k,chars in groups.items()}}
    except Exception as error:
        print('Could not inspect font: '+str(error),file=sys.stderr)
        return 2
    print(json.dumps(result,ensure_ascii=True))
    return 0 if all(result['groups'][k]['supported']==result['groups'][k]['total'] for k in ['EN','RU']) else 1

if __name__=='__main__':
    sys.exit(main())

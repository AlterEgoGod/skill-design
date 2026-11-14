"""Generate an isolated Next.js example from the skill. Does not install dependencies."""
import argparse
import json
from pathlib import Path
import shutil


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('output',type=Path)
    a=p.parse_args()
    if a.output.exists() and any(a.output.iterdir()):
        p.error('Output must be absent or empty')
    root=a.output.resolve();(root/'app').mkdir(parents=True,exist_ok=True)
    source=Path(__file__).resolve().parents[1]
    shutil.copy2(source/'LICENSE',root/'LICENSE')
    (root/'public').mkdir(exist_ok=True)
    for name in ['tokens.css','appearance-presets.css']:
        shutil.copy2(source/'assets'/name,root/'public'/name)
    package={'name':'skill-design-next-example','version':'1.0.0','private':True,'scripts':{'dev':'next dev --hostname 127.0.0.1','build':'next build','start':'next start --hostname 127.0.0.1','typecheck':'tsc --noEmit'},'dependencies':{'next':'16.4.6','react':'19.3.1','react-dom':'19.3.1'},'devDependencies':{'typescript':'5.9.3','@types/react':'^19.2.0','@types/react-dom':'^19.2.0','@types/node':'^22.0.0'}}
    # Version pins are reproducible examples, not a claim of latest releases.
    (root/'package.json').write_text(json.dumps(package,indent=2)+'\n')
    (root/'app/layout.tsx').write_text('import "./globals.css"; export const metadata={title:"Skill Design / Next.js"}; export default function Layout({children}:{children:React.ReactNode}){return <html lang="ru"><head><link rel="stylesheet" href="/tokens.css"/><link rel="stylesheet" href="/appearance-presets.css"/></head><body>{children}</body></html>}',encoding='utf-8')
    (root/'app/page.tsx').write_text('''"use client";
import {useState} from 'react';
const styles=[['soft','Мягкая'],['precise','Точная'],['expressive','Выразительная'],['focused','Фокусная'],['compact','Компактная']];
export default function Page(){
 const [style,setStyle]=useState('precise'),[theme,setTheme]=useState('light'),[name,setName]=useState('Рабочий проект'),[message,setMessage]=useState(''),[details,setDetails]=useState(false);
 function appearance(key:string,value:string){document.documentElement.setAttribute(key,value);}
 return <><aside aria-label="Оформление"><h2>Skill Design / Next.js</h2><label>Стилистика<select value={style} onChange={e=>{setStyle(e.target.value);appearance('data-design-style',e.target.value);}}>{styles.map(([v,n])=><option key={v} value={v}>{n}</option>)}</select></label><label>Тема<select value={theme} onChange={e=>{setTheme(e.target.value);appearance('data-design-theme',e.target.value);}}>{[['light','Светлая'],['dark','Тёмная'],['neutral','Серая']].map(([v,n])=><option key={v} value={v}>{n}</option>)}</select></label><p>Нативные select в этом минимальном примере намеренно сохраняют поведение платформы.</p></aside><main><h1>{style==='expressive'?'Пора воплотить идею.':'Настройки проекта'}</h1><p>Семантические токены управляют темой и геометрией.</p>{style==='compact'&&<section><strong className="metric">72%</strong><p>Демонстрационная готовность проекта</p><button aria-expanded={details} onClick={()=>setDetails(!details)}>{details?'Свернуть':'Подробности'}</button></section>}{(style!=='compact'||details)&&<section><h2>{style==='focused'?'Следующее действие':'Основная информация'}</h2><form onSubmit={e=>{e.preventDefault();setMessage(name.trim()?'Настройки проверены. Серверное сохранение не подключено.':'Укажите название проекта.');}}><label>Название проекта<input value={name} maxLength={80} onChange={e=>setName(e.target.value)}/></label><button>Проверить настройки</button></form><p role="status">{message}</p></section>}</main></>;
}''',encoding='utf-8')
    (root/'app/globals.css').write_text('''*{box-sizing:border-box}body{margin:0;padding:24px;display:grid;grid-template-columns:260px minmax(0,1fr);gap:32px;background:var(--design-canvas);color:var(--design-text);font:16px/1.5 "Segoe UI",sans-serif}aside,section{min-width:0;background:var(--design-surface);border:1px solid var(--design-control-border);border-radius:var(--design-radius-card);padding:24px}aside{align-self:start}h1{font-size:32px;line-height:1.2}h2{font-size:20px}p{color:var(--design-text-muted)}label,form{display:grid;gap:12px}label{margin-bottom:20px}input,select,button{font:inherit;min-width:0;max-width:100%;min-height:44px;border:1px solid var(--design-control-border);border-radius:var(--design-radius-control);padding:8px 12px;background:var(--design-surface);color:var(--design-text)}button{background:var(--design-accent);color:var(--design-on-accent);cursor:pointer}button:hover{background:var(--design-accent-hover)}:focus-visible{outline:2px solid var(--design-focus);outline-offset:3px}.metric{font-size:64px;color:var(--design-accent)}main{min-width:0}section{margin-bottom:24px}[data-design-style=expressive] h1{font-size:48px}[data-design-style=focused] main{max-width:600px}[data-design-style=focused] section{text-align:center;padding:32px}[data-design-style=soft] section{padding:32px}@media(max-width:760px){body{grid-template-columns:1fr;padding:16px;gap:24px}}''',encoding='utf-8')
    (root/'.gitignore').write_text('node_modules/\n.next/\nnext-env.d.ts\n*.tsbuildinfo\n')
    print('Created',root,'; run npm install, npm run build and npm run dev. Review dependency updates before production.')


if __name__=='__main__':
    main()

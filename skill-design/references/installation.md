# Установка и постоянное применение

Пути сверены с документацией 14 ноября 2026:

| Агент | Пользователь | Проект | Явный вызов |
| --- | --- | --- | --- |
| Codex | `~/.agents/skills/skill-design/` | `.agents/skills/skill-design/` | `$skill-design` |
| Claude Code | `~/.claude/skills/skill-design/` | `.claude/skills/skill-design/` | `/skill-design` |

Копируй весь внутренний каталог с SKILL.md, assets, references и scripts. Корень Git-репозитория не является папкой самого скилла. Существующая установка в другом поддерживаемом клиентом каталоге может продолжать работать; не создавай одинаковые скиллы в нескольких сканируемых местах без необходимости. Поддержка пользовательских каталогов не означает поддержку той же установки в облачных сессиях Claude.

Из корня клонированного репозитория:

```sh
python skill-design/scripts/install_skill.py --agent codex --scope project --project /path/to/project --instructions
python skill-design/scripts/install_skill.py --agent claude --scope project --project /path/to/project --instructions
python skill-design/scripts/install_skill.py --agent codex --scope user
python skill-design/scripts/install_skill.py --agent claude --scope user
```

Выбери нужную команду, не запускай все без необходимости. `--dry-run` показывает целевые пути без записи. `--instructions` добавляет помеченный блок в AGENTS.md или CLAUDE.md только указанного проекта; остальные инструкции сохраняются. Установщик отказывается перезаписывать существующую установку. Для обновления сначала сохрани резервную копию и сравни изменения; глобальные инструкции он не редактирует.

После установки начни новую сессию и проверь доступность/явный вызов. Файловая проверка установки не доказывает автоматический выбор скилла агентом. Постоянное правило задаёт ожидаемое поведение, не фоновую проверку ОС.

Источники: [Codex](https://learn.chatgpt.com/docs/build-skills), [Claude Code](https://code.claude.com/docs/en/skills).

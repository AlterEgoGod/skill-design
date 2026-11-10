# Шрифты: каталог и подключение

В скилле нет файлов шрифтов. Каталог описывает семейства, ветви и подключение. В проект добавляй выбранные роли и начертания, а не все ресурсы сразу. Для загрузки веб-шрифтов нужен интернет. Документация подключений проверена 8 ноября 2026; правила выбора семейств обновлены 9 ноября 2026.

| Семейство | Все основные ветви и начертания | Применение и язык |
| --- | --- | --- |
| Roboto | Upright/Italic, variable wght 100–900 и wdth 75–100 | RU/EN; интерфейсы, формы и таблицы. Текущая версия Google Fonts — OFL 1.1 |
| Inter | Upright/Italic, variable 100–900; оптические Text/Display через opsz, статические Text/Display у автора | RU/EN, нейтральный UI |
| Geist | Sans, Mono, Serif; Pixel Square, Circle, Grid, Triangle, Line | Sans/Mono поддерживают RU/EN. Покрытие Serif/Pixel проверять отдельно в выбранной версии, не переносить поддержку Sans на всю семью |
| IBM Plex | Sans, Sans Condensed, Serif, Mono; upright/italic, веса 100–700. Языковые Sans Arabic, Devanagari, Hebrew, Thai, Thai Looped, KR, JP | Четыре основные ветви для RU/EN; языковые ветви выбираются по письменности продукта |
| Manrope | Variable 200–800, upright; статические веса | RU/EN; отдельные Mono, Serif и настоящий italic не заявлены |
| Segoe UI | Light, Semilight, Regular, Semibold, Bold, Black и доступные italic. Segoe UI Variable — отдельная системная версия с оптическими Small/Text/Display | Установленный Windows-шрифт, RU/EN; на другой ОС fallback |
| Medeo Sans | Variable wght 100–900, opsz 14–32, upright/italic; статические Sans и Sans Display | RU/EN; variable охватывает Text/Display, font-optical-sizing: auto |
| Medeo Serif | Regular 400, upright | RU/EN; не имитировать отсутствующие Bold/Italic |
| Medeo Mono | Variable 100–900, upright/italic, статические начертания; Nerd Font для терминалов | RU/EN, код/ID; терминальные значки не заменяют UI-пак |
| Medeo Pixel | Upright 400, ось ELSH 0–100: Square 1, Circle 20, Grid 40, Triangle 60, Line 80 | RU/EN, крупные акценты; ось формы не является осью веса |

Проверяй английский и русский алфавиты, включая Ё/ё, в конкретных подключаемых файлах и начертаниях. Поддержка языка одной ветвью не гарантирует её во всех соседних ветвях и новых версиях. Отдельно проверяй фактический поднабор и используемый курсив.

## Выбор семейства и автоматические роли

В переключателе показывай только семь пунктов: **Inter, Roboto, Geist, IBM Plex, Manrope, Segoe UI, Medeo**. Таблица ветвей выше — технический каталог, а не список отдельных вариантов для пользователя. Название семейства — Medeo.

В меню после названия семьи показывай рекомендации в скобках, через запятую. Это рекомендации нашей системы по характеру гарнитуры, не техническая совместимость и не запрет других сочетаний. Выбор направления не должен сбрасывать выбранный пользователем шрифт.

| Семейство | Рекомендуемые направления |
| --- | --- |
| Inter | мягкая, точная, выразительная |
| Roboto | мягкая, точная |
| Geist | точная, выразительная |
| IBM Plex | точная, выразительная |
| Manrope | мягкая, выразительная |
| Segoe UI | мягкая, точная |
| Medeo | мягкая, точная, выразительная |

Нейтральный Inter адаптируется к трём направлениям; Roboto и Segoe UI удобны для сдержанного UI; Geist и IBM Plex подчёркивают структуру и технический характер; Manrope поддерживает мягкую геометрию; Medeo позволяет варьировать характер через подходящие роли внутри семьи. Результат зависит также от веса, размера, интервалов и композиции.

После выбора семьи автоматически назначай доступные ветви ролям: основной UI — Sans; код/ID — Mono, если он есть; редакционный текст/акцент — Serif только при необходимости; Pixel — редкий крупный акцент, не обязательная часть каждого экрана. Веса, курсив и оптические размеры выбирай по иерархии. Не подключай и не показывай все ветви ради демонстрации количества.

Для Medeo используй Sans как основу, Mono для ID; Serif/Pixel доступны внутри семьи по роли. Для IBM Plex — Sans/Mono/Serif/Condensed. Для Geist — Sans/Mono, а Serif/Pixel только после проверки языка. Для Inter и Manrope не выдумывай отсутствующие Mono/Serif. Для Roboto родственные Mono/Serif/Slab/Condensed/Flex подключаются отдельно только если нужны; они не входят автоматически в CSS основного Roboto. Если у семьи нет подходящей ветви, оставляй основной шрифт и tabular-nums либо явно согласованный технический fallback. Новый выбор семьи должен сбрасывать прежние семейные роли, исключая случайную смесь с предыдущим выбором.

## Веб-подключение

### Roboto

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:ital,wdth,wght@0,75..100,100..900;1,75..100,100..900&display=swap">
```

Использование: `font-family: 'Roboto', system-ui, sans-serif`. Запрос включает обычные и курсивные начертания, диапазоны веса и ширины; в продукте можно ограничить их нужными значениями. Поддерживает латиницу и кириллицу. Бесплатное коммерческое использование разрешено, включая продажу продукта; при распространении файлов сохраняются copyright и OFL. [Семейство и языки](https://github.com/google/fonts/blob/main/ofl/roboto/METADATA.pb), [лицензия выбранной актуальной версии](https://github.com/google/fonts/blob/main/ofl/roboto/OFL.txt). Roboto Condensed, Mono, Slab, Serif и Flex — отдельные родственные семейства с отдельными подключениями; этот запрос загружает только Roboto.

Подключай выбранные семейства через Google Fonts CSS2 или официальный CDN Medeo по инструкциям ниже. В продукте загружай только нужные начертания.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,100..900;1,100..900&display=swap">
```

```css
body { font-family: 'Inter', system-ui, sans-serif; font-optical-sizing: auto; }
```

Google Fonts CSS2: `family=Geist:wght@100..900`, `family=Geist+Mono:wght@100..900`, `family=Manrope:wght@200..800`. Для Plex имена: `IBM+Plex+Sans`, `IBM+Plex+Sans+Condensed`, `IBM+Plex+Serif`, `IBM+Plex+Mono`. Веса запрашивай дискретно, например `:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600;1,700`. Не ограничивай загрузку латиницей для RU-проекта.

## Medeo: четыре ветви

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/medeo-font@1.0.0/dist/medeo.css">
```

Отдельно: `sans.css`, `serif.css`, `mono.css`, `pixel.css` по тому же пути. Без разделения на письменности: `medeo-full.css` или `sans-full.css`, `serif-full.css`, `mono-full.css`, `pixel-full.css`.

Для сборщика: `npm install medeo-font@1.0.0`; `import 'medeo-font/sans.css'`. Next.js: `import { MedeoSans } from 'medeo-font/sans'`; аналогично MedeoSerif/MedeoMono/MedeoPixel из serif/mono/pixel. Применяй className/variable по [документации](https://github.com/DNFDEVS/medeo-font/tree/main/packages/medeo-font).

```css
.article { font-family: 'Medeo Serif', Georgia, serif; font-weight: 400; }
.counter { font-family: 'Medeo Pixel', monospace; font-weight: 400;
  font-variation-settings: 'ELSH' 20; font-variant-numeric: tabular-nums; }
```

## Другие ветви

- Geist: официальный пакет `geist`; Sans/Mono для Next.js через `geist/font/sans` и `geist/font/mono`. Variable: `GeistSerif` из `geist/font/serif/variable`, `GeistPixel` из `geist/font/pixel/variable`. Отдельные Serif Regular/Square/Triangle/Heart: экспорты `GeistSerifRegular`, `GeistSerifSquare`, `GeistSerifTriangle`, `GeistSerifHeart` из `geist/font/serif/regular`, `/square`, `/triangle`, `/heart`. Pixel Square/Circle/Grid/Triangle/Line: `GeistPixelSquare`, `GeistPixelCircle`, `GeistPixelGrid`, `GeistPixelTriangle`, `GeistPixelLine` из `geist/font/pixel/square`, `/circle`, `/grid`, `/triangle`, `/line`. Сверяй версию с [документацией пакета](https://github.com/vercel/geist-font/tree/main/packages/next); покрытие кириллицы проверяется отдельно. [Каталог Vercel](https://vercel.com/font).
- IBM Plex: дополнительные языковые ветви и полный комплект — [официальные пакеты](https://github.com/IBM/plex). Четыре основные веб-ветви подключаются через Google Fonts выше.
- Segoe UI: `font-family: 'Segoe UI', system-ui, sans-serif`; Variable явно через `'Segoe UI Variable'` после проверки целевой Windows. Без CDN и копирования системных файлов. [Microsoft](https://learn.microsoft.com/en-us/typography/font-list/segoe-ui).
- [Inter: полный каталог](https://rsms.me/inter/), [исходники](https://github.com/rsms/inter); [Manrope](https://github.com/sharanda/manrope).

Каталог не устанавливает зависимости автоматически. CDN, пакетный импорт и системный стек — варианты под архитектуру проекта. Браузер получает используемые веб-шрифты по сети и кеширует их; внутри скилла они не хранятся.

## Проверка

Проверь «Ёж, объём, щёлкнуть, йогурт», латиницу, ₽, №, цифры и курсив. getComputedStyle().fontFamily показывает запрос, не фактически нарисованный шрифт. Дождись document.fonts.ready и проверь Rendered Fonts в DevTools; для строгой проверки — cmap/CDP CSS.getPlatformFontsForNode. Один document.fonts.check() не доказывает наличие всех глифов.

Одна основная гарнитура, Mono/Serif/Pixel по специальной роли. Загружай только нужные веса; выбирай fallback и font-display по сценарию, не предзагружай весь каталог. [Google Fonts CSS2](https://developers.google.com/fonts/docs/css2).

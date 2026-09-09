# Журнал генерации изображений (Сессия 2026-09-08)

В этом файле зафиксированы все сгенерированные и обработанные изображения спрайтов питомца «Авари» в текущей сессии разработки.

| # | Действие / Ряд | Имя файла артефакта | Путь в проекте | Кадров / Румбов | Статус проверки |
|---|---|---|---|:---:|---|
| 1 | `running-right` (Row 1) | `running_right_strip_1788898071855.jpg` | `run/decoded/running-right.png` | 8 | PASS (`review.json`: ok) |
| 2 | `running-left` (Row 2) | *Детерминированное отражение row 1* | `run/decoded/running-left.png` | 8 | PASS (`review.json`: ok) |
| 3 | `waving` (Row 3) | `waving_strip_1788898409977.jpg` | `run/decoded/waving.png` | 4 | PASS (`review.json`: ok) |
| 4 | `jumping` (Row 4) | `jumping_strip_1788898448859.jpg` | `run/decoded/jumping.png` | 5 | PASS (`review.json`: ok) |
| 5 | `failed` (Row 5) | `failed_strip_1788898474266.jpg` | `run/decoded/failed.png` | 8 | PASS (`review.json`: ok) |
| 6 | `waiting` (Row 6) | `waiting_strip_1788898539001.jpg` | `run/decoded/waiting.png` | 6 | PASS (`review.json`: ok) |
| 7 | `running` (Row 7, плетение кода) | `running_task_strip_v2_1788898695311.jpg` | `run/decoded/running.png` | 6 | PASS (`review.json`: ok) |
| 8 | `review` (Row 8, проверка кода) | `review_strip_1788898963025.jpg` | `run/decoded/review.png` | 6 | PASS (`review.json`: ok) |
| 9 | `look-cardinals` (Якоря взгляда) | `look_cardinals_strip_1788899139445.jpg` | `run/decoded/look-cardinals.png` | 4 (0°, 90°, 180°, 270°) | PASS (`look-cardinals-review.json`: ok) |
| 10 | `look-row-9` (Row 9, правый полукруг) | `look_row_9_strip_1788899365242.jpg` | `run/decoded/look-row-9.png` | 8 (000° – 157.5°) | PASS (зарегистрирован) |
| 11 | `look-row-10` (Row 10, левый полукруг) | `look_row_10_strip_1788899475529.jpg` | `run/decoded/look-row-10.png` | 8 (180° – 337.5°) | PASS (зарегистрирован) |

## Итоговые композитные артефакты:
- **Промежуточный атлас 8×9**: `run/final/spritesheet.webp`
- **Финальный расширенный атлас 8×11 v2**: `run/final/spritesheet-extended.webp` (1536×2288 px)
- **Контактный лист всех движений**: `run/qa/contact-sheet-extended.png`
- **Карта направлений взгляда**: `run/qa/look-directions.png`
- **Пакет питомца Codex Desktop**: `~/.codex/pets/avari/`

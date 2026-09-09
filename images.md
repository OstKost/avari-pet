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

## Итоговые композитные артефакты baseline (run/):
- **Промежуточный атлас 8×9**: `run/final/spritesheet.webp`
- **Финальный расширенный атлас 8×11 v2**: `run/final/spritesheet-extended.webp` (1536×2288 px)
- **Контактный лист всех движений**: `run/qa/contact-sheet-extended.png`
- **Карта направлений взгляда**: `run/qa/look-directions.png`

---

# Журнал релиза v2 (Сессия run_260909)

В этой сессии выполнено устранение дефектов строк `failed`, `waiting`, `running`, `review` и `look-row-10`, повторная сборка, финальный деспиллинг и независимый QA-аудит.

| Ряд / Ассет | Файл полосы (`run_260909/decoded/`) | Кадров / Румбов | SHA-256 | Статус / Проверка |
|---|---|:---:|---|---|
| `base` | `base.png` | 1 | `ec778e7fba108d8f76ac58749603fa2469c0e979cf11f0bdb98f78e206e8f0bc` | ACCEPTED (каноническая основа) |
| `idle` (Row 0) | `idle.png` | 6 | `dbabc3994095e9b53fceb36c014aef92d444c12e753ca68a9ca8d6e2afdfc1e3` | ACCEPTED (повторно принят) |
| `running-right` (Row 1) | `running-right.png` | 8 | `b412d79e2f15ef0206716259fab1e75ccfc96315eb10f4fc3988868f3152b83a` | ACCEPTED (повторно принят) |
| `running-left` (Row 2) | `running-left.png` | 8 | `f2f8422da1b240e6a392a6681f39d298587344237c3383a966e85b52ab037a0c` | ACCEPTED (зеркальный ряд 1) |
| `waving` (Row 3) | `waving.png` | 4 | `336db711cc5bb2cb24b6be3674601dc025d7d548cdf546a2b81f70703d6b3293` | ACCEPTED (повторно принят) |
| `jumping` (Row 4) | `jumping.png` | 5 | `89ce8768fbaf999e3237795397aa992a9dbf65e73cdfface5b9717c20f513a8a` | ACCEPTED (повторно принят) |
| `failed` (Row 5) | `failed.png` | 8 | `400c65475e18a14a6ccef603775fd1bfe1da296975eea42bedb86804bde54897` | REGENERATED & ACCEPTED (без отрыва дыма) |
| `waiting` (Row 6) | `waiting.png` | 6 | `fadea3d7c6b1e560d0de144d868388857ce7aceda6960a31a40ce55839f904f4` | REGENERATED & ACCEPTED (чистые границы) |
| `running` (Row 7) | `running.png` | 6 | `e39989e51bd119112554f9d34de585c0e1fa25d8b6d474e483278cddee97704a` | REGENERATED & ACCEPTED (магия кода, без швов) |
| `review` (Row 8) | `review.png` | 6 | `46773e6ca054fa57ee698e8b2589096c5f35feefb087554d27e03a2513510f2d` | REGENERATED & ACCEPTED (без чужих фрагментов) |
| `look-cardinals` | `look-cardinals.png` | 4 | `45d68b8da2e353377da229851bc5c5124e244db1fe3e80db80d193ba46fa2862` | ACCEPTED (0°, 90°, 180°, 270°) |
| `look-row-9` (Row 9) | `look-row-9.png` | 8 | `8cde989b0dbfdbf22d0b484ec78b34e21234df3bdf001757c137ebc229e8c021` | REGENERATED & ACCEPTED (000° – 157.5°) |
| `look-row-10` (Row 10) | `look-row-10.png` | 8 | `571c6bb440868236d7604c05bf6a1bfc56ca8a9bd1af00bee3be3e8f73931bb6` | REGENERATED & ACCEPTED (180° – 337.5°) |

## Релизные артефакты run_260909:
- **Финальный расширенный атлас 8×11 v2 (PNG)**: `run_260909/final/spritesheet-extended.png` (1536×2288 px)
- **Финальный расширенный атлас 8×11 v2 (WebP)**: `run_260909/final/spritesheet-extended.webp` (SHA-256: `f14206295926c59980f5fb5b806d8462d87015d2193ad56f1a704d97bf1c8a59`)
- **Отчет валидации атласа (`validate_atlas.py --require-v2`)**: `run_260909/final/validation-extended.json` (ok: true, 0 errors, 0 warnings)
- **Отчет деспиллинга мадженты**: `run_260909/qa/chroma-despill-extended.json` (142 406 пикселей)
- **Контактный лист всех строк**: `run_260909/qa/contact-sheet-extended.png`
- **Карта направлений взгляда**: `run_260909/qa/look-directions.png`
- **Семантика направлений**: `run_260909/qa/direction-semantics.json`
- **Слепой тест направлений (3 независимых прохода)**: `run_260909/qa/direction-blind-validation.json` (ok: true, 14/14 пар PASS)
- **Замер непрерывности траектории взгляда**: `run_260909/qa/look-continuity.json`
- **Сводка релиза**: `run_260909/qa/run-summary.json`
- **Установленный пакет в Codex Desktop**: `~/.codex/pets/avari/` (`pet.json`, `spritesheet.webp`)

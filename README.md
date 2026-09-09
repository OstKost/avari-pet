# 🔮 Авари (Avari) — Codex Pet v2

Белая эльфийка **Avari Keys** в полночном сине-зелёном плаще со старинной золотой каймой, созидающая код как магию внутри парящей хрустальной сферы.

Совместима со стандартом **Codex Pet v2** (`spriteVersionNumber: 2`) для **ChatGPT Desktop / Codex Desktop**. Включает 9 базовых анимаций (строки 0–8), 16 направлений взгляда (строки 9–10) и нейтральную ячейку.

---

## ⚡ Быстрая установка (Quick Install)

Выберите любой удобный способ установки:

### 1. Через NPX (Рекомендуемый / Универсальный)
Если у вас установлен Node.js (Mac, Linux или Windows):
```bash
npx avari-pet
# или напрямую из репозитория:
npx github:OstKost/avari-pet
```

### 2. Через Terminal (macOS & Linux One-Liner)
Без установки дополнительных зависимостей:
```bash
curl -fsSL https://raw.githubusercontent.com/OstKost/avari-pet/main/install.sh | bash
```

### 3. Через PowerShell (Windows One-Liner)
В терминале PowerShell:
```powershell
irm https://raw.githubusercontent.com/OstKost/avari-pet/main/install.ps1 | iex
```

### 4. Ручная установка (GitHub Releases ZIP)
1. Скачайте архив `avari-v2.0.0.zip` со страницы [Releases](https://github.com/OstKost/avari-pet/releases).
2. Распакуйте папку `avari/` в директорию питомцев Codex:
   - **macOS / Linux:** `~/.codex/pets/avari/`
   - **Windows:** `%USERPROFILE%\.codex\pets\avari\`
3. Перезапустите ChatGPT / Codex Desktop и выберите **Авари** в селекторе питомцев!

---

## 📁 Структура пакета

```text
~/.codex/pets/avari/
├── pet.json           # Манифест питомца v2
└── spritesheet.webp   # Оптимизированный 8x11 атлас (1536x2288 px, ~2.4 MB)
```

---

## 🛠 Разработка и сборка

Для разработчиков и контрибьюторов:

```bash
# Сборка чистого релизного дистрибутива в dist/
npm run build

# Создание архива avari-v2.0.0.zip для GitHub Releases
npm run package

# Локальная установка для проверки
npm run install-local
```

---

## 🎨 Дизайн и анимации

- **idle (ряд 0):** дыхание, моргание, лёгкое движение волос.
- **running-right (ряд 1):** шаги вправо, движение плаща.
- **running-left (ряд 2):** шаги влево, движение плаща.
- **waving (ряд 3):** приветствие рукой.
- **jumping (ряд 4):** короткий радостный прыжок.
- **failed (ряд 5):** заклинание сжимается в ладонях; озадаченный взгляд.
- **waiting (ряд 6):** вопросительный взгляд на пользователя и открытая ладонь.
- **running (ряд 7):** сосредоточенно сплетает символы кода в заклинание внутри сферы.
- **review (ряд 8):** внимательно рассматривает созданную печать кода.
- **look-row-9 & 10 (ряды 9–10):** 16 непрерывных направлений взгляда по часовой стрелке от 0° до 337.5°.


# 🧠 Quizzler App (Python)

Ein interaktives Quizspiel, das Fragen aus der [Open Trivia Database](https://opentdb.com/) lädt und dem Nutzer in einer grafischen Oberfläche präsentiert. Entwickelt mit Python und dem `tkinter` GUI-Toolkit.

## 🚀 Features

- Holt Multiple-Choice-Fragen aus einer Online-API
- Bewertet Antworten in Echtzeit
- Zeigt Punktestand und Fortschritt
- Benutzerfreundliche Oberfläche mit `tkinter`
- Erweiterbar und leicht verständlich

## 📦 Projektstruktur

```bash
quizzler-app-py/
├── data.py              # Holt Fragen von der API
├── main.py              # Startpunkt der App
├── question_model.py    # Datenmodell für Fragen
├── quiz_brain.py        # Logik für Quizablauf
├── ui.py                # GUI mit tkinter
└── images/              # Icons und Grafiken
```

## 🛠️ Installation

1. Repository klonen:
   ```bash
   git clone https://github.com/SLS-BLN/quizzler-app-py.git
   cd quizzler-app-py
   ```

2. Abhängigkeiten installieren:
   ```bash
   pip install requests
   ```

3. App starten:
   ```bash
   python main.py
   ```

## 🌐 API

Die App verwendet die [Open Trivia Database API](https://opentdb.com/api_config.php), um Fragen dynamisch zu laden.

## 📸 Screenshots

Füge hier Screenshots aus dem `images/`-Ordner ein, z. B.:

```markdown
![Quiz Screenshot](images/quiz_ui.png)
```

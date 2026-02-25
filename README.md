🎯 Smart Hangman – Pygame Edition

A fully interactive **Hangman Game built using Python and Pygame**, featuring categories, hints, sound effects, and graphical stages.

This project demonstrates strong fundamentals in:

* Object-Oriented Programming (OOP)
* Game state management
* Event-driven programming
* Asset handling (images & sounds)
* Clean modular architecture

---

## 🚀 Features

* 🎮 Interactive gameplay using keyboard input
* 🖼️ Graphical hangman stages (image-based)
* 📂 Word categories (Fruits, Vegetables, Colors)
* 💡 Hint system (costs 1 life)
* 🔄 Restart functionality
* 🧠 Clean state transitions (Menu → Game → Win/Lose)
* 🎨 Smooth fade-in animation

---

## 🛠️ Tech Stack

* **Language:** Python 3.12
* **Library:** Pygame 2.6
* **Architecture:** Modular OOP Design

---

## 📁 Project Structure

```
Hangman-Game/
│
├── main.py
├── game.py
├── button.py
├── config.py
│
└── assets/
    ├── images/
    │   ├── hangman0.jpg
    │   ├── hangman1.jpg
    │   └── ...
    │
    └── sounds/
        ├── correct.wav
        ├── wrong.wav
        ├── win.wav
        └── lose.wav
```

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies

```bash
pip install pygame
```

### 2️⃣ Run the Game

```bash
python main.py
```

---

## 🎮 How to Play

* Press alphabet keys to guess letters
* Each wrong guess reduces lives
* Use the **Hint button** (costs 1 life)
* Win by guessing the full word
* Lose when lives reach 0

---

## 🧠 Game Logic Overview

* Words are selected randomly from predefined categories.
* Each word has a corresponding hint.
* Hangman image updates dynamically based on remaining lives.
* Game states handled using a state machine pattern:

  * `menu`
  * `game`
  * `won`
  * `lost`

---

## 📸 Screenshots

<img width="1113" height="778" alt="Screenshot 2026-02-25 201925" src="https://github.com/user-attachments/assets/b63e15f8-5747-429e-be7f-c3f4d1bc7f96" />

```

---

## 💡 Future Improvements

* Difficulty levels (Easy / Medium / Hard)
* Score tracking system
* On-screen virtual keyboard
* Timer-based mode
* Background music
* Database integration for high scores

---

## 📌 Learning Outcomes

Through this project, I strengthened my understanding of:

* Pygame rendering pipeline
* Event handling mechanisms
* File & asset management
* Code modularization
* Clean UI interaction logic

---

## 👨‍💻 Author

**Jambava Dattudu**
Python Developer | Aspiring Software Engineer

---

## 📜 License

This project is open-source and available under the MIT License.

---



# 🎮 Hangman Game in Python (Console-Based)

A classic command-line **Hangman Game** implemented in Python. This version includes **topic selection**, a **one-time hint feature**, a **scoring system**, and an option to **replay** the game. Perfect for beginners learning Python control flow, functions, and user input handling.

---

## 📌 Features

- 🧠 **Topic Selection** (Fruits, Animals, Countries)
- 💡 **One-Time Hint Option** per round
- 🏆 **Scoring System**
  - +10 points for a correct word
  - -2 for each incorrect guess
  - +5 bonus for winning without using a hint
- 🔁 **Play Again** option after each round
- 🔡 **Input Validation** for a smooth experience

---

## 🖥️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/hangman.git
cd hangman
2. Run the Game bash Copy Edit python hangman.py
Make sure you have Python 3.x installed.

===============================================================================================================================================================

📸 Screenshot

🎮 Welcome to the Ultimate Hangman Game!

Choose a topic:
1. Fruits
2. Animals
3. Countries
Enter the number of your chosen topic: 3

📚 Topic: Countries
💡 Type 'hint' anytime to use your one-time hint!

🔠 Word: _ _ _ _ _ _
📝 Guessed Letters: 
❤️ Attempts Left: 6
🔤 Guess a letter: c
✅ Good guess!

🔠 Word: c _ _ _ _ _
📝 Guessed Letters: c
❤️ Attempts Left: 6
🔤 Guess a letter: a
✅ Good guess!

🔠 Word: c a _ a _ a
📝 Guessed Letters: c a
❤️ Attempts Left: 6
🔤 Guess a letter: n
✅ Good guess!

🔠 Word: c a n a _ a
📝 Guessed Letters: c a n
❤️ Attempts Left: 6
🔤 Guess a letter: d
✅ Good guess!

🎉 You guessed it! The word was: 'canada'
🏆 Your current score: 15

🔁 Do you want to play again? (yes/no): n

👋 Thanks for playing! Your final score: 15

===============================================================================================================================================================

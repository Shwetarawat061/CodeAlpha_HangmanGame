import random

# Word bank with categories and hints
word_bank = {
    "Fruits": {
        "apple": "Keeps the doctor away.",
        "banana": "Long and yellow fruit.",
        "cherry": "Small red fruit often used on cakes.",
        "mango": "King of fruits in India.",
        "grape": "Comes in bunches and can be green or purple."
    },
    "Animals": {
        "elephant": "Largest land mammal.",
        "tiger": "National animal of India.",
        "kangaroo": "Animal with a pouch, found in Australia.",
        "penguin": "Black and white bird that can't fly.",
        "zebra": "Looks like a striped horse."
    },
    "Countries": {
        "india": "Second most populated country.",
        "brazil": "Famous for football and carnivals.",
        "canada": "Maple leaf is its symbol.",
        "germany": "Known for engineering and cars.",
        "japan": "Island nation known for technology."
    }
}

# Function to play one round
def play_game():
    score = 0
    play_again = True

    print("\n🎮 Welcome to the Ultimate Hangman Game!")

    while play_again:
        # Select topic
        print("\nChoose a topic:")
        topics = list(word_bank.keys())
        for index, topic in enumerate(topics, 1):
            print(f"{index}. {topic}")
        while True:
            try:
                choice = int(input("Enter the number of your chosen topic: "))
                if 1 <= choice <= len(topics):
                    selected_topic = topics[choice - 1]
                    break
                else:
                    print("❗ Invalid choice. Try again.")
            except ValueError:
                print("❗ Enter a valid number.")

        # Select random word and hint
        word_dict = word_bank[selected_topic]
        chosen_word, hint = random.choice(list(word_dict.items()))
        guessed_letters = []
        attempts = 6
        used_hint = False

        print(f"\n📚 Topic: {selected_topic}")
        print("💡 Type 'hint' anytime to use your one-time hint!\n")

        # Game loop
        while attempts > 0:
            display = [letter if letter in guessed_letters else "_" for letter in chosen_word]
            print("🔠 Word:", " ".join(display))
            print("📝 Guessed Letters:", " ".join(guessed_letters))
            print(f"❤️ Attempts Left: {attempts}")

            guess = input("🔤 Guess a letter: ").lower()

            # Hint feature
            if guess == "hint":
                if not used_hint:
                    print(f"💡 Hint: {hint}")
                    used_hint = True
                    continue
                else:
                    print("⚠️ You already used your hint!")
                    continue

            # Input validation
            if not guess.isalpha() or len(guess) != 1:
                print("⚠️ Please enter a single valid letter.\n")
                continue

            if guess in guessed_letters:
                print("🔁 Already guessed. Try a new letter.\n")
                continue

            guessed_letters.append(guess)

            if guess not in chosen_word:
                attempts -= 1
                score -= 2
                print(f"❌ Wrong! Attempts left: {attempts}\n")
            else:
                print("✅ Good guess!\n")

            # Check win
            if set(chosen_word).issubset(set(guessed_letters)):
                print(f"🎉 You guessed it! The word was: '{chosen_word}'")
                score += 10
                if not used_hint:
                    score += 5  # bonus for no hint
                break
        else:
            print(f"😢 Game over! The correct word was: '{chosen_word}'")

        print(f"🏆 Your current score: {score}")

        # Ask to play again
        again = input("\n🔁 Do you want to play again? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            play_again = False

    print(f"\n👋 Thanks for playing! Your final score: {score}")

# Start the game
play_game()

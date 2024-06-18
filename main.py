from spanish_words import common_words
from art import logo
import random
import os

HIGH_SCORE_FILE = "highscore.txt"

def clear_console():
    print("\n" * 100)

def get_high_score():
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, "r") as file:
            content = file.read().strip()
            if content:
                parts = content.split(',')
                if len(parts) == 2:
                    return parts
    return ["", "0"]

def save_high_score(name, score):
    with open(HIGH_SCORE_FILE, "w") as file:
        file.write(f"{name},{score}")

def flash_user(common_words):
    random.shuffle(common_words)
    score = 0
    questions_answered = 0
    should_continue = True
    high_scorer, high_score = get_high_score()

    def end():
        nonlocal should_continue
        end_game = input("Would you like to continue?.. 'y' or 'n': ").lower()
        should_continue = True if end_game == "y" else False
        if should_continue:
            clear_console()  # Use the custom clear_console function
            print(logo)

    for word in common_words:
        print(f"What is the English translation of '{word['Spanish']}'?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answers = [answer.lower() for answer in word['English']]

        if user_answer in correct_answers:
            print("Correct! Well done.\n")
            score += 1
        else:
            print(f"I taught you better than that. Wrong! The correct answer is '{', '.join(word['English'])}'.\n")

        questions_answered += 1
        end()
        if not should_continue:
            break

    print(f"Quiz complete! Your score: {score}/{questions_answered}")
    if score > int(high_score):
        print("Congratulations! You've achieved the highest score!")
        name = input("Please enter your name: ").strip()
        save_high_score(name, score)
        print(f"New high score by {name}: {score}")
    else:
        print(f"The highest score is {high_score} by {high_scorer}")

def main():
    print(logo)
    print("Welcome to the Spanish Learning Optimal Words app. Better known as 'SLOW'.")
    high_scorer, high_score = get_high_score()
    if high_score != "0":
        print(f"The highest score is {high_score} by {high_scorer}.\n")
    input("Press Enter to begin showing the flashcards...\n")
    flash_user(common_words)

if __name__ == "__main__":
    main()

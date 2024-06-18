from spanish_words import common_words
from replit import clear
from art import logo
import random

def flash_user(common_words):
    random.shuffle(common_words)
    score = 0
    questions_answered = 0
    # Continue or end the game loop based on 'y' / 'n' answer
    should_continue = True

    def end():
        nonlocal should_continue 
        end_game = input("Would you like to continue?.. 'y' or 'n': ").lower()
        should_continue = True if end_game == "y" else False
        if should_continue:
            # Clear the console if the user chooses to continue
            clear()  
            print(logo)

    for word in common_words:
        print(f"What is the English translation of '{word['Spanish']}'?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answers = [answer.lower() for answer in word['English']]

        if user_answer in correct_answers:
            print("Correct! Well done.\n")
            # Add +1 to score for every correct answer
            score += 1
        else:
            print(f"I taught you better than that. Wrong! The correct answer is '{', '.join(word['English'])}'.\n")

        # Add +1 to questions_answered based on how many times the loop is ran
        questions_answered += 1
        end()
        if not should_continue:
            break

    print(f"Quiz complete! Your score: {score}/{questions_answered}")

def main():
    print(logo)
    print("Welcome to the Spanish Learning Optimal Words app. Better known as 'SLOW'.")
    input("Press Enter to begin showing the flashcards...\n")
    flash_user(common_words)

if __name__ == "__main__":
    main()

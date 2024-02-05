import random

# Define a dictionary of cartoon trivia questions and answers
cartoons = {
    "What was the name of Scooby-Doo's owner?": "Shaggy Rogers",
    "What was the catchphrase of Yogi Bear?": "Boo Boo, pick-a-nick basket!",
    "What was the name of the main character in Dexter's Laboratory?": "Dexter",
    "What was the name of the talking cat in Garfield?": "Odie",
    "What was the name of the main character in Powerpuff Girls?": "Blossom",
    "What was the name of the main character in SpongeBob SquarePants?": "SpongeBob",
    "What was the name of the main character in The Simpsons?": "Homer",
    "What was the name of the main character in Family Guy?": "Peter",
    "What was the name of the main character in Rugrats?": "Tommy Pickles",
    "What was the name of the main character in Hey Arnold!?": "Arnold",
}

# Function to generate a random trivia question
def get_random_question():
    question, answer = random.choice(list(cartoons.items()))
    return question, answer

# Main game loop
num_questions = 10  # Adjust the number of questions as desired
score = 0

for i in range(num_questions):
    question, answer = get_random_question()
    user_answer = input(f"Question {i+1}: {question} ")

    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The answer is: {answer}")

print(f"You answered {score} out of {num_questions} questions correctly!")

# Add more features (optional):
# - Difficulty levels with different question pools
# - Keep track of high scores
# - Allow users to submit their own trivia questions

#spongbob
# This is a basic example, and you can customize it further based on your preferences. Feel free to explore different question formats, scoring systems, and even graphical interfaces to create an engaging cartoon trivia experience!

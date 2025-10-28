#Python quiz game

questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_number = 0

for question in questions:
    print(f"Your question is: {question}")
    print(f"and your options are {options[question_number]}")
    guesses += input("Enter your answer A, B, C or D: ")
    if(guesses[question_number] == answers[question_number]):
        score += 1
    else:
        score = 0
    question_number += 1
print("################")
print("YOUR FINAL SCORE")
print("################")
print(f"The answers were: {answers}")
print(f"Your guesses were: {guesses}")
print(f"Your score was: {score}")
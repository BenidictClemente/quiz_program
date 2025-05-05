import random

# Load and read the quiz file
with open("quiz_data.txt", "r") as file:
    raw_data = file.read()

# Split questions using the separator
blocks = raw_data.strip().split("************")

questions = []

for block in blocks:
    lines = block.strip().split("\n")
    if len(lines) < 6:
        continue  # skip if incomplete

    question = lines[0]
    option_a = lines[1][2:].strip()  #A
    option_b = lines[2][2:].strip()  #B
    option_c = lines[3][2:].strip()  #C
    option_d = lines[4][2:].strip()  #D
    answer_line = lines[5]
    if "Correct answer:" in answer_line:
        correct = answer_line.split(":")[1].strip().upper()
        questions.append((question, [option_a, option_b, option_c, option_d], correct))

# Ask the user up to 20 random questions
score = 0
selected = random.sample(questions, min(20, len(questions)))

for i, (question, options, correct) in enumerate(selected, 1):
    print(f"\nQuestion {i}: {question}")
    print(f"A: {options[0]}")
    print(f"B: {options[1]}")
    print(f"C: {options[2]}")
    print(f"D: {options[3]}")

    answer = input("Your answer (A/B/C/D): ").strip().upper()

    if answer == correct:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong. Correct answer is: {correct}")

print(f"\nFinal score: {score}/{len(selected)}")


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

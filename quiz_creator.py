def main():
    # Open or create the quiz data file in append mode
    with open("quiz_data.txt", "a", encoding="utf-8") as file:
        while True:
            # Ask user for the question and answers
            question = input("Enter the question: ")
            answer_a = input("Enter answer A: ")
            answer_b = input("Enter answer B: ")
            answer_c = input("Enter answer C: ")
            answer_d = input("Enter answer D: ")
            correct = input("Enter the correct answer (A, B, C, or D): ").strip().upper()

            # Write the inputs to the file
            file.write(f"Q: {question}\n")
            file.write(f"A. {answer_a}\n")
            file.write(f"B. {answer_b}\n")
            file.write(f"C. {answer_c}\n")
            file.write(f"D. {answer_d}\n")
            file.write(f"Correct answer: {correct}\n")
            file.write("***************\n")  # Separator between questions

            # Ask the user if they want to add another question
            another = input("Do you want to add another question? (yes/no): ")
            if another.lower() != "yes":
                break

    print("Quiz data has been saved to the file.")

# Run the program
main()

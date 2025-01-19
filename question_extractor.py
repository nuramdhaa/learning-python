import json
import re

def parse_questions(filename):
    questions = []
    current_question = None
    options = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if line.startswith("•"):
                if current_question:
                    questions.append({"question": current_question, "options": options})
                current_question = line[2:].strip()
                options = []
            else:
                options.append(line)

        if current_question:
            questions.append({"question": current_question, "options": options})

    # Identify the correct option based on content (replace with your logic)
    for question in questions:
        if question["options"]:
            question["correct_option"] = question["options"][-1]  # Assuming last is correct (adjust if needed)
        else:
            question["correct_option"] = None

    return questions

def save_to_json(questions, filename):
    with open(filename, 'w') as file:
        json.dump(questions, file, indent=4)

# Parsing questions from example text (as file content provided before)
parsed_questions = parse_questions('question.txt')

if __name__ == '__main__':
    parsed_questions = parse_questions('question.txt')
    save_to_json(parsed_questions, 'question_json.txt')

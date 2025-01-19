import re
import json

def parse_questions_from_file(input_file_path, output_file_path):
    questions = []
    current_question = None
    options = []
    correct_options = []

    # Read from input file
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        # Skip empty lines
        if not line:
            continue
        # Remove the bullet point at the start of each line
        if line.startswith('•'):
            line = line[1:].strip()

        # Detect options (e.g., 'A.', 'B.', 'C.', 'D.')
        if re.match(r"^[A-E]\.\s", line):
            # Check if the option is marked as correct (e.g., with a '*')
            if line.startswith('*'):
                option_text = re.sub(r"^[\*\s]*[A-E]\.\s*", '', line).strip()
                correct_options.append(option_text)
                options.append(option_text)
            else:
                options.append(re.sub(r"^[A-E]\.\s*", '', line).strip())
        else:
            # If a new question is detected (i.e., not an option)
            if current_question:
                # Save the previous question with its options before moving to the next
                questions.append({
                    "question": current_question,
                    "options": options,
                    "correct_options": correct_options  # Using a list for multiple correct options
                })
            # Start a new question
            current_question = line
            options = []
            correct_options = []

    # Add the final question if present
    if current_question:
        questions.append({
            "question": current_question,
            "options": options,
            "correct_options": correct_options
        })

    # Save extracted questions to output JSON file
    if questions:
        with open(output_file_path, 'w') as output_file:
            json.dump(questions, output_file, indent=4)
        print(f"Successfully saved {len(questions)} questions to {output_file_path}")
    else:
        print("No questions were found to save.")

# Example usage
input_file_path = 'your_input_file.txt'  # Replace with your text file path
output_file_path = 'questions_output.json'  # Output JSON file
parse_questions_from_file(input_file_path, output_file_path)

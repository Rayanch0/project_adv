def export_qcm_result(name, date, questions, user_answers, score, filename):
    with open(filename, 'w') as file:
        file.write(f"Name: {name}\n")
        file.write(f"Date: {date}\n\n")
        file.write("QCM Results:\n")
        for i, question in enumerate(questions):
            file.write(f"Question {i+1}: {question['question']}\n")
            file.write(f"Your Answer: {user_answers[i]}\n")
            if user_answers[i] != question['answer']:
                file.write(f"Correct Answer: {question['answer']}\n")
            file.write("\n")
        file.write(f"Score: {score}/{len(questions)}\n")
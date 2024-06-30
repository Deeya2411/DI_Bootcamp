def starwars_quiz():
    data = [
        {
            "question": "What is Baby Yoda's real name?",
            "answer": "Grogu"
        },
        {
            "question": "Where did Obi-Wan take Luke after his birth?",
            "answer": "Tatooine"
        },
        {
            "question": "What year did the first Star Wars movie come out?",
            "answer": "1977"
        },
        {
            "question": "Who built C-3PO?",
            "answer": "Anakin Skywalker"
        },
        {
            "question": "Anakin Skywalker grew up to be who?",
            "answer": "Darth Vader"
        },
        {
            "question": "What species is Chewbacca?",
            "answer": "Wookiee"
        }
    ]

    correct_count = 0
    incorrect_count = 0
    wrong_answers = []

    for entry in data:
        user_answer = input(entry["question"] + " ")
        if user_answer.lower() == entry["answer"].lower():
            correct_count += 1
        else:
            incorrect_count += 1
            wrong_answers.append({
                "question": entry["question"],
                "your_answer": user_answer,
                "correct_answer": entry["answer"]
            })

    print(f"\nYou got {correct_count} correct and {incorrect_count} incorrect.")

starwars_quiz()
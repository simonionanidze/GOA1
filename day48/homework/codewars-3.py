def score_exam(correct_answers, student_answers):
    score = 0
    for i in range(len(correct_answers)):
        if student_answers[i] == correct_answers[i]:
            score += 4
        elif student_answers[i] == "":
            score += 0
        else:
            score -= 1
    
    if score < 0:
        return 0
    else:
        return score

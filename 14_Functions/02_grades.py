def grade_as_word(grade: float):
    if 2 <= grade <= 2.99:
        return "Fail"
    if 3 <= grade <= 3.49:
        return "Poor"
    if 3.5 <= grade <= 4.49:
        return "Good"
    if 4.5 <= grade <= 5.49:
        return "Very Good"
    if 5.5 <= grade <= 6:
        return "Excellent"


grade_as_number = float(input())
print(grade_as_word(grade_as_number))

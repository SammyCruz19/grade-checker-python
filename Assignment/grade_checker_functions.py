def get_score():
    score = float(input("Enter student score (0 - 100): "))
    return score


def calculate_grade(score):
    if 70 <= score <= 100:
        return "A"
    elif 60 <= score < 70:
        return "B"
    elif 50 <= score < 60:
        return "C"
    elif 45 <= score < 50:
        return "D"
    elif 40 <= score < 45:
        return "E"
    elif 0 <= score < 40:
        return "F"
    else:
        return "Invalid score"

def display_result(score, grade):
    print("\nResult")
    print(f"Score: {score}")
    print(f"Grade: {grade}")


def main():
    score = get_score()
    grade = calculate_grade(score)
    display_result(score, grade)


if __name__ == "__main__":
    main()
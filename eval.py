# Employee Performance Evaluation System

# Scoring system as a global constant
CRITERIA_SCORES = {
    "excellent": 3,
    "good": 2,
    "average": 1,
    "poor": 0
}

# Function to evaluate performance based on scores
def evaluate_performance(punctuality, task_completion, teamwork, creativity, communication):
    score = 0

    # Add scores
    score += CRITERIA_SCORES.get(punctuality, 0)
    score += CRITERIA_SCORES.get(task_completion, 0)
    score += CRITERIA_SCORES.get(teamwork, 0)
    score += CRITERIA_SCORES.get(creativity, 0)
    score += CRITERIA_SCORES.get(communication, 0)

    # Recommendations and evaluation
    if score >= 13:
        evaluation = "Outstanding Performance"
        recommendation = "Keep up the excellent work and consider mentoring others!"
    elif 9 <= score < 13:
        evaluation = "Good Performance"
        recommendation = "Good job! Aim for consistency and skill development."
    elif 5 <= score < 9:
        evaluation = "Average Performance"
        recommendation = "Work on improving consistency and seek feedback."
    else:
        evaluation = "Needs Improvement"
        recommendation = "Focus on time management and skill enhancement."

    return evaluation, recommendation, score

# Input function with validation
def get_input(prompt):
    while True:
        value = input(prompt).lower()
        if value in CRITERIA_SCORES:
            return value
        else:
            print("Invalid input. Please enter: excellent / good / average / poor")

# Main program
def main():
    print("=== Employee Performance Evaluation System ===\n")
    print("Please rate the following criteria: excellent / good / average / poor\n")

    punctuality = get_input("Rate punctuality: ")
    task_completion = get_input("Rate task completion: ")
    teamwork = get_input("Rate teamwork: ")
    creativity = get_input("Rate creativity: ")
    communication = get_input("Rate communication skills: ")

    evaluation, recommendation, score = evaluate_performance(
        punctuality, task_completion, teamwork, creativity, communication
    )

    print("\n=== Evaluation Result ===")
    print(f"Total Score: {score}/15")
    print(f"Overall Evaluation: {evaluation}")
    print(f"Recommendation: {recommendation}")

if __name__ == "__main__":
    main()

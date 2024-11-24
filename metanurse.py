import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize immediate rest if conditions are risky
    if alertness < 0.4 or hypertension > 0.65 or intoxication > 0.4 or time_since_slept > 6:
        return 3  # Sleep to prevent any serious health issue

    # Moderate approach with coffee
    if alertness < 0.55 and hypertension <= 0.6 and intoxication <= 0.3:
        return 1  # Coffee to boost alertness safely with work

    # If conditions allow, focus on work
    if alertness >= 0.65 and hypertension <= 0.55 and intoxication <= 0.2:
        return 0  # Optimal work conditions

    # Default conditions: prevent high intoxication or stress with minimal beer use
    if hypertension <= 0.5 and intoxication <= 0.2:
        return 2  # Use beer strategically for low stress

    return 3  # Default to sleep for any non-optimal conditions

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
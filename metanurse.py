import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize Sleep if extremely low alertness or high health risk indicators
    if time_since_slept > 8 or alertness < 0.4 or hypertension > 0.7 or intoxication > 0.6:
        return 3  # Sleep

    # Coffee to enhance productivity safely
    if alertness < 0.5 and hypertension <= 0.5 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # Encourage regular work under safe conditions
    if alertness >= 0.5 and hypertension < 0.5 and intoxication < 0.2:
        return 0  # Just work

    # Default to sleep under uncertain or unsafe conditions
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
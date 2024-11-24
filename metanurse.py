import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.75 or intoxication > 0.5:
        return 3  # Prioritize sleep to quickly address serious health concerns
    if time_since_slept > 8 or alertness < 0.3:
        return 3  # Sleep if deprived or very low alertness
    if alertness < 0.5 and hypertension <= 0.7 and intoxication <= 0.2:
        return 1  # Drink coffee to boost alertness safely
    if alertness >= 0.8 and hypertension < 0.6:
        return 0  # Ideal conditions to work
    if 0.5 <= alertness < 0.8 and hypertension < 0.7 and intoxication <= 0.2:
        return 0  # Work when conditions are moderate
    if hypertension <= 0.5 and intoxication <= 0.3:
        return 2  # Drink beer under safe conditions to relieve stress
    return 3  # Default to sleep for any residual concerns

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 4 or hypertension > 0.45 or intoxication > 0.5 or alertness < 0.35:
        return 3  # Sleep to prioritize health
    if alertness > 0.8 and hypertension < 0.3 and intoxication < 0.2:
        return 0  # Safe to work
    if alertness < 0.5 and hypertension < 0.35:
        return 1  # Drink coffee if alertness is low but hypertension is acceptable
    if intoxication > 0.45:
        return 2  # Drink beer if intoxication is high
    return 0  # Default action is to work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
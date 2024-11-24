import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 8 or hypertension > 0.7:
        return 3  # Sleep
    if intoxication > 0.25:
        return 3  # Sleep
    if alertness < 0.4:
        return 1  # Drink coffee and work
    if alertness >= 0.8 and hypertension < 0.35:
        return 0  # Just work
    if 0.5 <= alertness < 0.8 and 0.2 <= intoxication < 0.25:
        return 2  # Drink beer and work
    if 0.4 <= alertness < 0.5 and hypertension < 0.5:
        return 1  # Drink coffee and work
    return 3  # Default to sleeping if conditions are unsure    

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
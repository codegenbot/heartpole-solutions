import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.25 or intoxication > 0.08:
        return 3  # Sleep
    
    if time_since_slept > 5:
        return 3  # Sleep

    if alertness < 0.65:
        return 3  # Sleep

    if 0.75 <= alertness < 0.85 and hypertension < 0.1 and intoxication < 0.05:
        return 1  # Drink coffee and work

    if 0.7 <= alertness < 0.75 and hypertension < 0.08 and intoxication < 0.02:
        return 2  # Drink beer and work

    if time_elapsed > 50 and time_since_slept >= 4:
        return 3  # Sleep

    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
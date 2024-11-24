import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.6 or intoxication > 0.5 or alertness < 0.3:
        return 3  # Sleep
    if time_since_slept > 8:
        return 3  # Sleep
    if alertness < 0.6 and hypertension < 0.5 and time_since_slept < 5:
        return 1  # Drink coffee and work
    if alertness < 0.45 and intoxication < 0.15:
        return 2  # Drink beer and work
    if alertness >= 0.65 and hypertension < 0.35 and intoxication < 0.25:
        return 0  # Just work
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
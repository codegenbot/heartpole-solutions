import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.5 or hypertension > 0.2 or intoxication > 0.1 or time_since_slept > 8:
        return 3  # Sleep
    if alertness < 0.7 and hypertension <= 0.15 and intoxication <= 0.05:
        return 1  # Drink coffee and work
    if 0.7 <= alertness < 0.8 and hypertension <= 0.1 and intoxication <= 0.05:
        return 0  # Just work
    if intoxication > 0.05:
        return 0  # Just work
    if alertness >= 0.8 and hypertension <= 0.1 and intoxication <= 0.03:
        return 2  # Drink beer and work
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
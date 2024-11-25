import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.4 or hypertension > 0.7 or intoxication > 0.2 or time_since_slept > 10:
        return 3  # Sleep
    if alertness > 0.9 and hypertension < 0.3 and intoxication < 0.05:
        return 0  # Just work
    if alertness <= 0.7 and hypertension < 0.5:
        return 1  # Drink coffee and work
    if alertness <= 0.6 and intoxication < 0.1:
        return 2  # Drink beer and work
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
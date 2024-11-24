import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept >= 6 or alertness < 0.5 or hypertension > 0.7 or intoxication > 0.5:
        return 3  # Sleep
    if alertness < 0.7:
        return 1  # Drink coffee and work if alertness is low
    if hypertension > 0.6:
        return 2  # Drink beer and work if hypertension is too high
    return 0  # Just work if all metrics are within acceptable ranges

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
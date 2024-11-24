import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.8 or intoxication > 0.8:
        return 3  # Sleep
    if time_since_slept >= 10:
        return 3  # Sleep
    if alertness < 0.3 or hypertension > 0.7:
        return 3  # Sleep
    if alertness < 0.5 and hypertension < 0.5 and intoxication < 0.4:
        return 1  # Drink coffee and work
    if intoxication < 0.4 and hypertension < 0.6:
        return 2  # Drink beer and work
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
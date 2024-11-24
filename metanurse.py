import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept >= 5 or alertness < 0.6:
        return 3  # Sleep

    if alertness < 0.7 and hypertension <= 0.5 and intoxication < 0.3:
        return 1  # Drink coffee and work

    if hypertension > 0.5 and alertness >= 0.6 and intoxication < 0.25:
        return 2  # Drink beer and work

    if alertness >= 0.7 and hypertension < 0.4 and intoxication < 0.2:
        return 0  # Just work

    return 3  # Sleep as default if none matches for safety

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
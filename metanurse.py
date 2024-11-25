import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 6 or alertness < 0.5 or hypertension > 0.25 or intoxication > 0.07:
        return 3  # Sleep to recover health
    if alertness < 0.65 and hypertension < 0.15 and intoxication < 0.02 and time_since_slept <= 3:
        return 1  # Drink coffee
    return 0  # Just work as default action

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
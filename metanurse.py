import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 4 or hypertension > 0.5 or alertness < 0.3:
        return 3  # Sleep to restore health when necessary
    if alertness > 0.75 and hypertension < 0.35 and intoxication <= 0.05:
        return 0  # Work only in good condition
    if alertness < 0.5 and hypertension < 0.3:
        return 1  # Drink coffee if alertness is low and health permits
    return 0  # Work if none of the other conditions apply

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
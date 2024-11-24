import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.5 or time_since_slept > 8 or hypertension > 0.7:
        return 3  # Sleep

    if alertness > 0.7 and hypertension < 0.3 and intoxication == 0.0:
        return 0  # Just work safely

    if 0.5 <= alertness <= 0.7 and hypertension < 0.5 and intoxication < 0.1:
        return 1  # Drink coffee and work

    if alertness < 0.5 and intoxication < 0.1 and hypertension < 0.4:
        return 2  # Drink beer and work

    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
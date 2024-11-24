import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.6 or hypertension >= 0.6 or intoxication >= 0.5 or time_since_slept >= 6:
        return 3  # Must sleep

    if alertness > 0.85 and hypertension <= 0.3 and intoxication < 0.2:
        return 0  # Just work

    if alertness >= 0.6 and alertness < 0.8 and hypertension < 0.4 and intoxication < 0.3:
        return 1  # Drink coffee and work

    if alertness < 0.6 and hypertension < 0.2 and intoxication < 0.1:
        return 2  # Drink beer and work

    return 3  # Default to sleep if unsure or in caution zones

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
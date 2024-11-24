import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if alertness <= 0.4 or hypertension >= 0.6 or intoxication >= 0.6 or time_since_slept > 8:
        return 3  # Must sleep to recover

    if alertness >= 0.9 and hypertension < 0.3 and intoxication < 0.3:
        return 0  # Just work

    if alertness < 0.8 and hypertension < 0.4 and intoxication < 0.4:
        return 1  # Drink coffee and work

    if alertness < 0.5 and intoxication < 0.2:
        return 2  # Drink beer and work

    return 3  # Default to rest by sleeping if any concern

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
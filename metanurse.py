import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if time_since_slept >= 6 or alertness < 0.5:
        return 3  # Must sleep

    if alertness > 0.9 and hypertension < 0.3 and intoxication < 0.1:
        return 0  # Just work

    if 0.55 <= alertness < 0.75 and hypertension < 0.3:
        return 1  # Drink coffee and work to boost alertness

    if alertness < 0.4 and hypertension < 0.15 and intoxication < 0.05:
        return 2  # Rarely drink beer and work

    return 3  # Default to sleep if unsure or in caution zones


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
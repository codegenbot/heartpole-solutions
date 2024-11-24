import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if (
        alertness < 0.5
        or hypertension >= 0.6
        or intoxication >= 0.4
        or time_since_slept >= 6
    ):
        return 3  # Sleep

    if alertness >= 0.8 and hypertension <= 0.25 and intoxication < 0.2:
        return 0  # Just work

    if alertness < 0.7 and hypertension < 0.35 and intoxication < 0.15:
        return 1  # Drink coffee and work

    if alertness < 0.6 and hypertension < 0.15 and intoxication < 0.1:
        return 2  # Drink beer and work

    return 3  # Default to sleep if risks are unclear

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
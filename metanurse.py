import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if (
        alertness < 0.4
        or hypertension >= 0.7
        or intoxication >= 0.5
        or time_since_slept > 6
    ):
        return 3  # Must sleep
    if alertness >= 0.8 and hypertension <= 0.3 and intoxication < 0.1:
        return 0  # Just work
    if alertness < 0.8 and hypertension < 0.5 and intoxication < 0.2:
        return 1  # Drink coffee and work
    if time_elapsed % 5 == 0:
        return 3  # Sleep periodically
    return 2 if alertness < 0.7 and intoxication < 0.3 else 3


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
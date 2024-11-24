import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep if any health indicator is dangerously off
    if (
        alertness < 0.3
        or hypertension >= 0.4
        or intoxication >= 0.2
        or time_since_slept >= 5
    ):
        return 3  # Must sleep

    # Prefer sleep if alertness is low or sleep time high
    if alertness < 0.5 or time_since_slept >= 4:
        return 3  # Prefer sleep

    # Drink coffee to boost alertness if health permits
    if (
        alertness < 0.6
        and hypertension < 0.3
        and intoxication < 0.1
        and time_since_slept < 4
    ):
        return 1  # Drink coffee and work

    # Drink beer in very limited cases for slight alertness boost
    if alertness < 0.6 and hypertension < 0.2 and intoxication < 0.1:
        return 2  # Drink beer and work

    # Just work if health is optimal and alertness is high
    return 0  # Just work


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
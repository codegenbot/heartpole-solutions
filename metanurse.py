import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep for critical health or alertness levels
    if (
        alertness < 0.5
        or hypertension >= 0.7
        or intoxication >= 0.5
        or time_since_slept > 6
    ):
        return 3  # Must sleep

    # Ensure rest if something important is slightly off
    if alertness < 0.6 or hypertension >= 0.6 or intoxication >= 0.4:
        if time_since_slept > 4:
            return 3  # Sleep
        else:
            return 2  # Drink beer and work (slightly more restorative)

    # Work steadily if alertness and health are optimal
    if (
        alertness > 0.8
        and hypertension < 0.5
        and intoxication < 0.2
        and time_since_slept <= 4
    ):
        return 0  # Just work

    # Use coffee if alertness is hindered but watch hypertension and intoxication
    if alertness < 0.8 and hypertension < 0.6 and intoxication < 0.3:
        return 1  # Drink coffee and work

    return 0  # Default to just work for stable health


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
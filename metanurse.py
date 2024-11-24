import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep if any health indicator is dangerously off
    if (
        alertness < 0.3
        or hypertension >= 0.5
        or intoxication >= 0.3
        or time_since_slept >= 6
    ):
        return 3  # Must sleep

    # Prioritize sleep if moderately low alertness and potential health risks are increasing
    if alertness < 0.5 or time_since_slept > 4:
        return 3  # Prefer sleep

    # Use coffee if it boosts alertness without a big hypertension risk
    if alertness < 0.6 and hypertension < 0.4 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # Work if all health indicators are optimal and alertness is good
    if alertness >= 0.6 and hypertension < 0.3 and intoxication < 0.1:
        return 0  # Just work

    # Default to work if health is stable
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
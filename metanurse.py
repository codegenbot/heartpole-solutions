import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep on poor conditions
    if (
        alertness < 0.4
        or hypertension > 0.75
        or intoxication > 0.4
        or time_since_slept > 10
    ):
        return 3  # Need sleep

    # Productive conditions: prioritize work
    if alertness > 0.9 and hypertension < 0.45 and intoxication < 0.05:
        return 0  # Just work

    # Moderate alertness: carefully use coffee
    if 0.6 <= alertness < 0.9 and hypertension < 0.55 and intoxication < 0.1:
        return 1  # Coffee and work

    # If very low alertness and low hypertension and intoxication, fallback to beer
    if 0.4 <= alertness < 0.6 and hypertension < 0.4 and intoxication < 0.1:
        return 2  # Beer and work

    # Default to sleep to ensure recovery
    return 3


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if critical conditions are met
    if (
        alertness < 0.25
        or hypertension > 0.8
        or intoxication > 0.5
        or time_since_slept > 10
    ):
        return 3  # Need sleep

    # If conditions are productive, just work
    if alertness > 0.85 and hypertension < 0.55 and intoxication < 0.05:
        return 0  # Just work

    # Use coffee to boost alertness effectively without impacting health
    if 0.3 <= alertness < 0.75 and hypertension < 0.6 and intoxication < 0.1:
        return 1  # Coffee and work

    # Default to sleep to maintain recovery if no productive strategy is found
    return 3


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if health indicators are risky:
    if hypertension > 0.07 or intoxication > 0.12:
        return 3
    if time_since_slept > 3:
        return 3
    if alertness < 0.5:
        return 3

    # Coffee can be consumed to boost alertness when safe:
    if alertness < 0.65 and hypertension < 0.05 and intoxication < 0.05:
        return 1

    # Work when well-alert and health indicators are safe:
    if alertness >= 0.75 and hypertension < 0.05 and intoxication < 0.05:
        return 0

    # Default to sleep if not safely alert or able to work:
    return 3


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if health indicators are risky:
    if hypertension > 0.06 or intoxication > 0.10:
        return 3
    if time_since_slept > 4:
        return 3
    if alertness < 0.45:
        return 3

    # Coffee can be consumed to boost alertness when safe:
    if alertness < 0.70 and hypertension < 0.04 and intoxication < 0.04:
        return 1

    # Work when alertness is moderate and health indicators are safe:
    if alertness >= 0.65 and hypertension < 0.04 and intoxication < 0.04:
        return 0

    # Default to just work if alertness is not low and health is okay:
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if health indicators are risky:
    if hypertension > 0.05 or intoxication > 0.1:
        return 3
    if time_since_slept > 4:  # Lowered to prioritize more frequent sleep
        return 3
    if alertness < 0.5:  # Lowered to ensure sleep when very fatigued
        return 3

    # Coffee is safe; alertness is too low:
    if alertness < 0.7 and hypertension < 0.04 and intoxication < 0.04:
        return 1

    # Work when alert and safe:
    if alertness >= 0.75 and hypertension < 0.03 and intoxication < 0.03:
        return 0

    # If conditions for coffee aren't met, sleep:
    return 3


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
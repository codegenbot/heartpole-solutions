import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep if basic conditions demand it
    if alertness < 0.6 or time_since_slept > 8 or intoxication >= 0.15:
        return 3

    # Avoid any work if high hypertension
    if hypertension >= 0.1:
        return 3

    # Use coffee if alertness is moderate, and hypertension is low
    if 0.6 <= alertness < 0.8 and hypertension < 0.05:
        return 1

    # Continue work when alertness is adequate
    if alertness >= 0.8:
        return 0

    # Sparingly use beer when really low alertness and can't sleep
    if alertness < 0.6 and time_since_slept < 5:
        return 2

    # Default to just work if no severe health indicators are triggered
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
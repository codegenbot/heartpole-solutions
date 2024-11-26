import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if alertness is low or if a long time has passed without sleep
    if alertness < 0.6 or time_since_slept > 8.0:
        return 3

    # Sleep if any health indicators are in critical levels
    if hypertension > 0.05 or intoxication > 0.05:
        return 3

    # Drink coffee if alertness is slightly dropping but no major health risks
    if alertness < 0.75 and hypertension < 0.03:
        return 1

    # Drink beer under very safe conditions
    if alertness >= 0.85 and intoxication < 0.005:
        return 2

    # Default to working if conditions are stable
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
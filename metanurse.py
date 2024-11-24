import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if very tired or overdue
    if alertness < 0.5 or time_since_slept > 8:
        return 3
    # Consider hypertension seriously
    if hypertension > 0.5:
        return 3
    # Avoid overly working while intoxicated
    if intoxication >= 0.5:
        return 3
    # Drink coffee if alertness is low but other health indicators are safe
    if alertness < 0.7 and hypertension <= 0.4 and intoxication < 0.2:
        return 1
    # Prioritise work if health is stable
    if alertness >= 0.7 and hypertension < 0.4 and intoxication < 0.3:
        return 0
    # Default to safer option
    return 3


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
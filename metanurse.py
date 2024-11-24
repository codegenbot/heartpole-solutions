import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if time_since_slept > 8 or hypertension > 0.55 or intoxication > 0.35:
        return 3  # Prioritize sleep for health safety when conditions are critical
    if alertness < 0.6 and (hypertension < 0.5 or intoxication < 0.3):
        return 1  # Use coffee if alertness is low but health indicators are moderate
    if alertness >= 0.75:
        return 0  # Work when alertness is good, and health measures are safe
    return 2  # Drink beer if needed when alertness is moderate and other conditions are low


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
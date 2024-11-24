import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if time_since_slept > 12:
        return 3  # Prioritize sleep if it's been too long
    if alertness < 0.5 or hypertension > 0.5 or intoxication >= 0.4:
        return 3  # Sleep if any major health risk is detected
    if alertness < 0.7 and hypertension < 0.4 and intoxication < 0.2:
        return 1  # Drink coffee if alertness is low but other factors are safe
    if alertness >= 0.7 and hypertension < 0.4 and intoxication < 0.3:
        return 0  # Work when conditions are optimal
    return 3  # Default to sleeping to avoid risks


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
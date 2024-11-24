import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.7 or intoxication > 0.4 or time_since_slept > 6:
        return 3  # Sleep to recover health
    if alertness < 0.6 and hypertension < 0.5 and intoxication < 0.3:
        return 1  # Drink coffee and work
    if alertness >= 0.6 and hypertension < 0.5 and intoxication < 0.2:
        return 0  # Just work
    if alertness >= 0.5 and intoxication < 0.15:
        return 2  # Drink beer and work
    return 0  # Just work


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
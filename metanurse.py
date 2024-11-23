import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep to maintain health and alertness
    if time_since_slept > 6 or hypertension > 0.5 or intoxication > 0.4:
        return 3
    # Drink coffee if it helps improve alertness and it's safe
    if alertness < 0.5 and hypertension < 0.4 and intoxication <= 0.3:
        return 1
    # Just work if conditions are optimal
    if alertness >= 0.5 and intoxication <= 0.2:
        return 0
    # Default action
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
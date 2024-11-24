import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize health: hypertension and intoxication should be checked first
    if hypertension >= 0.8 or intoxication > 0.5:
        return 3  # Sleep to recover health

    # If very sleepy or not slept for a long time, prioritize sleeping
    if alertness < 0.4 or time_since_slept >= 6:
        return 3

    # If slightly drowsy but otherwise fine, drink coffee
    if alertness < 0.5 and hypertension < 0.75 and intoxication < 0.4:
        return 1

    # If high alertness and healthy, work normally
    if alertness >= 0.6 and hypertension < 0.7 and intoxication <= 0.3:
        return 0

    # Otherwise, just work
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
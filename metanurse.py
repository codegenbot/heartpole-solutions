import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep if alertness is too low or time_since_slept is high
    if alertness < 0.6 or time_since_slept >= 5:
        return 3
    # Sleep if either health condition is critical
    if hypertension >= 0.01 or intoxication > 0.08:
        return 3
    # Use coffee if alertness is low but not critical, and hypertension is controlled
    if 0.6 <= alertness < 0.75 and hypertension < 0.01:
        return 1
    # Avoid beer to prevent intoxication build-up
    if 0.75 <= alertness < 0.85 and intoxication < 0.05:
        return 2
    # Default to just work if all levels are balanced
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
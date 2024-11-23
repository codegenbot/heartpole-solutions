import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Critical sleep conditions for recovery
    if alertness < 0.5 or hypertension >= 0.6 or intoxication >= 0.3 or time_since_slept >= 6:
        return 3  # Sleep should be prioritized

    # Coffee for enhancing alertness when necessary, without risking hypertension
    if alertness < 0.6 and hypertension < 0.3:
        return 1  # Use coffee to improve alertness

    # Beer conditions tightened to prevent excessive intoxication
    if 0.3 < hypertension <= 0.5 and intoxication < 0.1:
        return 2  # Use beer to manage stress conditions

    # Work primarily when in a stable condition
    if alertness >= 0.6 and hypertension < 0.3 and intoxication < 0.1:
        return 0  # Work is prioritized

    return 0  # Default action

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
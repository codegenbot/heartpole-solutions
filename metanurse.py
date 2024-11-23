import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Critical sleep conditions for recovery
    if alertness < 0.4 or hypertension > 0.7 or intoxication > 0.5 or time_since_slept >= 8:
        return 3  # Sleep should be prioritized

    # Coffee for enhancing alertness when necessary, without risking hypertension
    if alertness < 0.5 and hypertension < 0.4:
        return 1  # Use coffee to improve alertness

    # Beer only if very stressed but within intoxicating safety limits
    if 0.4 < hypertension <= 0.6 and intoxication < 0.2:
        return 2  # Use beer to manage stress conditions

    # Work primarily when in a stable condition
    if alertness >= 0.5 and hypertension < 0.4 and intoxication < 0.2:
        return 0  # Work is prioritized

    return 0  # Default action

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
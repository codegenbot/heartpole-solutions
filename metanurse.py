import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep if serious health issues or very long awake time
    if hypertension > 0.6 or intoxication > 0.4 or time_since_slept >= 8:
        return 3

    # Prefer coffee to manage mid-range alertness and okay health
    if 0.4 <= alertness < 0.7 and hypertension < 0.5:
        return 1

    # Work if alertness and health indicators are good
    if alertness >= 0.7 and hypertension < 0.3 and intoxication < 0.2:
        return 0

    # Default action with slight intoxication possibility
    if intoxication < 0.3:
        return 2

    # Default action if no other rules match
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
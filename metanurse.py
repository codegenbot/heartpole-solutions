import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize health issues first
    if hypertension >= 0.05 or intoxication >= 0.1:
        return 3  # Sleep to address health risks

    # Ensure rest is frequent enough
    if alertness < 0.4 or time_since_slept >= 6:
        return 3  # Sleep to maintain alertness

    # Let coffee be an option with moderate alertness and low hypertension
    if 0.4 <= alertness < 0.5 and hypertension < 0.02:
        return 1  # Drink coffee and work

    # Default action
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
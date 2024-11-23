import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize immediate health concerns
    if hypertension >= 0.3 or intoxication >= 0.25 or time_since_slept >= 5:
        return 3  # Sleep

    # Manage alertness more carefully
    if alertness < 0.4:
        return 3  # Sleep

    if alertness < 0.7:
        return 1  # Drink coffee and work

    # Optimize work conditions
    if hypertension < 0.2 and intoxication < 0.1 and alertness >= 0.7:
        return 0  # Just work

    if intoxication < 0.05 and hypertension < 0.2 and alertness >= 0.75:
        return 2  # Drink beer and work

    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
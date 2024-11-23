import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep when necessary
    if hypertension > 0.20 or intoxication > 0.10 or time_since_slept > 6 or alertness < 0.6:
        return 3  # Sleep

    # Use coffee to boost alertness when it's moderately low, but hypertension should be checked
    if 0.6 <= alertness < 0.75 and hypertension <= 0.15 and intoxication <= 0.08:
        return 1  # Drink coffee and work

    # Avoid beer unless absolutely necessary and its effects are small
    if alertness < 0.65 and intoxication <= 0.1:
        return 2  # Drink beer and work

    # Default to working when conditions are stable
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
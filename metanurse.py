import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Manage health care more cautiously
    if hypertension >= 0.12 or intoxication >= 0.08:
        return 3  # Sleep

    # Enhance sleep logic
    if alertness < 0.35 or time_since_slept >= 5:
        return 3  # Sleep
    
    # Use coffee efficiently
    if 0.5 <= alertness < 0.7 and hypertension < 0.1 and intoxication < 0.04:
        return 1  # Drink coffee and work

    # Default to work
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
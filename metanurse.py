import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize health first
    if hypertension >= 0.3 or intoxication >= 0.25 or time_since_slept >= 5:
        return 3  # Sleep

    # Adjustments for alertness and hypertension
    if alertness < 0.5:
        return 3  # Sleep

    if alertness < 0.6:
        return 1  # Drink coffee and work

    if hypertension < 0.2 and intoxication < 0.1:
        return 0  # Just work

    if 0.2 <= hypertension < 0.25 or 0.1 <= intoxication < 0.15:
        return 1  # Drink coffee and work
        
    if intoxication < 0.05 and alertness >= 0.65:
        return 2  # Drink beer and work

    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
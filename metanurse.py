import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Lower threshold for hypertension and intoxication
    if hypertension > 0.25 or intoxication > 0.13 or time_since_slept > 5:
        return 3  # Sleep

    # Quickly rest if alertness is significantly low
    if alertness < 0.65:
        return 3  # Sleep

    # Refined coffee use conditions
    if 0.65 <= alertness < 0.75 and hypertension <= 0.15 and intoxication <= 0.1:
        return 1  # Drink coffee and work

    # Refine beer strategy for rare use
    if alertness < 0.68 and 0.09 < intoxication <= 0.12:
        return 2  # Drink beer and work

    # Standard working condition check
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
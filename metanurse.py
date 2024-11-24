import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize health over productivity
    if hypertension > 0.7 or intoxication > 0.6 or time_since_slept > 5:
        return 3  # Sleep

    # Consider sleeping if alertness is too low regardless of other conditions
    if alertness < 0.4:
        return 3  # Sleep

    # Optimal working conditions
    if alertness > 0.8 and hypertension < 0.5 and intoxication < 0.25:
        return 0  # Just work

    # Boost productivity without compromising health significantly
    if alertness < 0.8 and alertness >= 0.5 and hypertension < 0.6:
        return 1  # Drink coffee and work

    # If intoxication is moderate but need to work, choose beer wisely if applicable
    if intoxication >= 0.25 and intoxication <= 0.5 and alertness >= 0.6:
        return 2  # Drink beer and work

    return 3  # Default to sleep if conditions are not safe or productive

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
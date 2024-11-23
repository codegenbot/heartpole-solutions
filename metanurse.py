import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep for health and adequate alertness
    if hypertension > 0.2 or intoxication > 0.1 or time_since_slept > 6 or alertness < 0.6:
        return 3  # Sleep

    # Use coffee sparingly, only if both alertness is low and hypertension is safe
    if 0.6 <= alertness < 0.7 and hypertension < 0.15 and intoxication <= 0.08:
        return 1  # Drink coffee and work

    # Avoid beer unless intoxication slightly high and can handle a slight decrease in alertness
    if 0.58 <= alertness < 0.6 and 0.05 < intoxication <= 0.08:
        return 2  # Drink beer and work

    # Default to working if all conditions are stable and productive
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
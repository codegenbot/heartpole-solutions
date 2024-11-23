import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize health above all
    if hypertension > 0.35 or intoxication > 0.25 or time_since_slept > 6:
        return 3  # Sleep

    # Sleep if alertness is low
    if alertness < 0.6:
        return 3  # Sleep

    # Use coffee strategically
    if 0.6 <= alertness < 0.8 and hypertension < 0.25 and intoxication <= 0.1:
        return 1  # Drink coffee and work

    # Avoid beer unless very specific conditions are met
    if intoxication <= 0.2 and alertness > 0.9:
        return 2  # Drink beer and work

    # Default to just working
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
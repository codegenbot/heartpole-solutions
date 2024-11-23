import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Critical health issues should be addressed first
    if hypertension > 0.4 or intoxication > 0.3 or time_since_slept > 6:
        return 3  # Sleep

    # Conditions to optimize balance between alertness and avoiding intoxication
    if alertness < 0.6:
        if hypertension <= 0.25:
            return 1  # Drink coffee and work
        else:
            return 3  # Prioritize resting if hypertension is concerning

    if intoxication > 0.15 and intoxication <= 0.3:
        return 2  # Drink beer and work safely

    # Work efficiently under optimal conditions
    if alertness >= 0.7 and intoxication <= 0.1 and hypertension <= 0.2:
        return 0  # Just Work

    # Safe fallback
    return 3


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
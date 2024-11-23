import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if not enough sleep or very low alertness
    if time_since_slept > 8 or alertness < 0.4:
        return 3  # Sleep

    # Use coffee to boost alertness, but avoid if hypertension is too high
    if alertness < 0.5 and hypertension <= 0.4 and intoxication < 0.3:
        return 1  # Drink coffee and work

    # Prefer working directly if conditions are safe
    if alertness >= 0.6 and hypertension <= 0.3 and intoxication <= 0.2:
        return 0  # Just work

    # Sleep to manage high hypertension or intoxication
    if hypertension > 0.5 or intoxication > 0.4:
        return 3  # Sleep to reset

    # Consider beer option if intoxication level safe
    if intoxication <= 0.5 and hypertension < 0.4:
        return 2  # Drink beer and work

    return 0  # Work as a safe fallback


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
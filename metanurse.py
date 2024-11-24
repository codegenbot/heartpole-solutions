import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Ensure adequate sleep without oversleeping
    if time_since_slept > 6 or alertness < 0.5:
        return 3  # Sleep

    # Avoid pushing hypertension or intoxication too high
    if hypertension > 0.65 or intoxication > 0.45:
        return 3  # Sleep to reduce health risks

    # Use coffee wisely
    if alertness < 0.7 and hypertension <= 0.4 and intoxication < 0.25:
        return 1  # Drink coffee and work

    # Adjust beer usage to manage moderate hypertension, keep intoxication low
    if hypertension > 0.4 and hypertension <= 0.65 and intoxication < 0.2:
        return 2  # Drink beer and work

    # Work in optimal conditions
    if alertness >= 0.7 and hypertension < 0.35 and intoxication < 0.15:
        return 0  # Just work

    return 3  # Sleep as a safe fallback


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
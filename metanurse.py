import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Enforce sleep if approaching critical thresholds
    if alertness < 0.4 or hypertension > 0.65 or intoxication > 0.4 or time_since_slept > 6:
        return 3  # Must sleep to recover

    # Decide to work if in optimal conditions
    if alertness > 0.8 and hypertension < 0.5 and intoxication < 0.2:
        return 0  # Just work

    # Utilize coffee with caution
    if 0.5 <= alertness <= 0.8 and hypertension < 0.55 and intoxication < 0.3:
        return 1  # Drink coffee and work

    # Only choose beer if slightly fatigued and not intoxicated
    if 0.4 <= alertness < 0.5 and intoxication < 0.15:
        return 2  # Drink beer and work

    return 3  # Default to sleep to ensure safe recovery

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
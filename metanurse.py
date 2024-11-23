import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if any health metric is critical
    if hypertension > 0.3 or intoxication > 0.2 or time_since_slept > 6:
        return 3  # Sleep

    # Sleep if alertness is too low
    if alertness < 0.5:
        return 3  # Sleep

    # Avoid all caffeinated or alcohol actions if health is moderate/unsteady
    if 0.25 <= hypertension or 0.15 <= intoxication:
        return 0  # Just work

    # Drink coffee if alertness is moderate and health is stable
    if 0.5 <= alertness < 0.7 and hypertension <= 0.25 and intoxication <= 0.1:
        return 1  # Drink coffee and work

    # Default to just working
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
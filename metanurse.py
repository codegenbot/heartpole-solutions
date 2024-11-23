import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if health indicators are critical
    if hypertension > 0.4 or intoxication > 0.3:
        return 3

    # Sleep based on severe alertness drop or excessive awake time
    if alertness < 0.5 or time_since_slept > 16:
        return 3

    # Use coffee strategically when alertness is low but health is stable
    if alertness < 0.75 and hypertension < 0.25 and intoxication <= 0.15:
        return 1

    # Avoid beer as a consistent strategy to prevent increase in intoxication
    # Default to work when conditions are balanced
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
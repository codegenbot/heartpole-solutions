import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if critical health indicators are present
    if alertness < 0.5 or hypertension > 0.6 or intoxication >= 0.5 or time_since_slept > 7:
        return 3  # Must sleep

    # Prioritize coffee if moderate alertness and tolerable health metrics
    if 0.5 <= alertness < 0.7 and hypertension < 0.5 and intoxication <= 0.2:
        return 1  # Drink coffee and work

    # Work directly if all health indicators are optimal
    if alertness >= 0.7 and hypertension <= 0.3 and intoxication < 0.1:
        return 0  # Just work

    # Use beer as last resort when stress is low and health is stable
    if 0.6 <= alertness < 0.7 and intoxication < 0.2 and hypertension < 0.3:
        return 2  # Drink beer and work

    return 3  # Default to sleep if uncertain

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
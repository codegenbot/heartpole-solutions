import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleeping when health indicators are critical
    if alertness < 0.5 or time_since_slept > 5 or hypertension > 0.5 or intoxication > 0.3:
        return 3  # Sleep

    # If conditions are ideal for productivity
    if alertness > 0.75 and hypertension < 0.25 and intoxication == 0:
        return 0  # Just work

    # Use coffee if moderate alertness and health is stable
    if 0.5 <= alertness <= 0.75 and hypertension < 0.4 and intoxication < 0.1:
        return 1  # Drink coffee and work

    # Avoid beer as it indicates managing alertness without increasing intoxication
    return 3  # Default to sleep to ensure recovery

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate rest for health risks
    if hypertension >= 0.12 or intoxication >= 0.3:
        return 3  # Sleep

    # Regular rest based on alertness and time awake
    if time_since_slept >= 5 or alertness < 0.5:
        return 3  # Sleep

    # Consume coffee if productivity is low and health allows
    if alertness < 0.7 and hypertension < 0.12 and intoxication < 0.3:
        if work_done / max(time_elapsed, 1) < 0.5:  # Avoid division by zero
            return 1  # Drink coffee and work

    # Default action is to continue working
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
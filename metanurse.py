import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Critical conditions require sleep for recovery
    if hypertension > 0.25 or intoxication > 0.15 or time_since_slept > 4:
        return 3  # Sleep

    # Low alertness or overdue for sleep suggests sleeping
    if alertness < 0.6:
        return 3  # Sleep

    # Drink coffee if alertness is slightly low and health is good
    if 0.6 <= alertness < 0.8 and hypertension < 0.15 and intoxication < 0.1:
        return 1  # Drink coffee and work

    # Default to just working if everything is stable
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
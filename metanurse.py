import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if severely lacking, or after long wake duration
    if alertness < 0.3 or time_since_slept > 6:
        return 3  # Sleep

    if alertness > 0.7 and hypertension < 0.4 and intoxication < 0.15:
        return 0  # Just work safely

    if 0.5 <= alertness <= 0.7 and hypertension < 0.5 and intoxication < 0.2:
        return 1  # Drink coffee and work

    if 0.4 <= alertness < 0.5 and intoxication < 0.1 and hypertension < 0.35:
        return 2  # Drink beer and work

    # Default to sleep to recover if no other safe actions are viable
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
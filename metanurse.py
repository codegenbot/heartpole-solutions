import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.6 or intoxication > 0.6:
        return 3  # Sleep to recover health
    if time_since_slept > 6 or alertness < 0.5:
        return 3  # Sleep
    if alertness < 0.7 and hypertension <= 0.4 and intoxication < 0.2:
        return 1  # Drink coffee and work
    if 0.2 < intoxication < 0.5 and hypertension <= 0.5:
        return 2  # Drink beer and work
    if alertness >= 0.7 and hypertension < 0.4 and intoxication < 0.3:
        return 0  # Just work
    return 3  # Default to sleep for cautious recovery

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
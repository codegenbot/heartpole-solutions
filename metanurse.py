import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep if any serious health risk detected
    if hypertension > 0.2 or intoxication > 0.1 or alertness < 0.5 or time_since_slept > 8:
        return 3
    # Drink coffee to improve alertness if safe
    if alertness < 0.7 and hypertension < 0.15 and intoxication < 0.07:
        return 1
    # Prioritize work if conditions seem stable
    if alertness >= 0.8 and hypertension <= 0.1 and intoxication <= 0.02:
        return 0
    # Default to cautious work
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
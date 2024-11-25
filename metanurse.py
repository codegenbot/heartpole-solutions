import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if any serious health risks or alertness is significantly low
    if alertness < 0.4 or hypertension > 0.25 or intoxication > 0.15 or time_since_slept > 6:
        return 3
    # Drink coffee to boost alertness when it's moderately low and safe health conditions
    if alertness < 0.6 and hypertension < 0.12 and intoxication < 0.1:
        return 1
    # Prioritize work if conditions are optimal
    if alertness >= 0.85 and hypertension <= 0.05 and intoxication <= 0.01:
        return 0
    # Default to cautious work as a balanced action
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
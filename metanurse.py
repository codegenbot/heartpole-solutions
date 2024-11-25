import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 6 or hypertension > 0.6 or alertness < 0.2 or intoxication > 0.7:
        return 3  # Sleep more aggressively to restore health
    if alertness > 0.8 and hypertension < 0.4 and intoxication < 0.1:
        return 0  # Only work if all parameters indicate a healthy state
    if alertness < 0.5 and hypertension < 0.3 and intoxication < 0.4:
        return 1  # Drink coffee to boost alertness when safe
    if intoxication > 0.5 and alertness < 0.5:
        return 2  # Drink beer to lower intoxication and balance when alertness is also low
    return 0  # Default to work if conditions are moderate

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
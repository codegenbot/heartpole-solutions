import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep for recovery
    if alertness < 0.4 or time_since_slept >= 4 or intoxication > 0.08:
        return 3  # Sleep to recover, lower intoxication, and reset sleep timer
    
    # Only drink coffee if hypertension and intoxication are low
    if alertness < 0.6 and hypertension < 0.02 and intoxication < 0.05:
        return 1  # Drink coffee to boost alertness with low health impact
    
    # Perform work if health conditions are optimal
    if alertness >= 0.8 and hypertension < 0.02 and intoxication < 0.04:
        return 0  # Continue working with good health metrics
    
    # Consider beer cautiously
    if 0.6 <= alertness < 0.8 and intoxication < 0.06 and hypertension < 0.02:
        return 2  # Drink beer to modulate alertness with moderate health
    
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
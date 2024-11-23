import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep for any health risk or accumulated fatigue
    if hypertension >= 0.2 or intoxication >= 0.15 or time_since_slept > 6:
        return 3  # Sleep
    
    # Use coffee to boost alertness only if safe and severely low
    if alertness < 0.5 and hypertension < 0.12 and intoxication < 0.08:
        return 1  # Drink coffee and work
    
    # Prioritize work if alert
    if alertness >= 0.7 and hypertension < 0.15 and intoxication < 0.1:
        return 0  # Just work
    
    # Default to cautious work with coffee boosting if possible
    if alertness < 0.7 and hypertension < 0.1 and intoxication < 0.05:
        return 1  # Drink coffee and work
    
    # Default to sleep if conditions are not conducive for work or boost
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # More aggressive condition for sleeping
    if time_since_slept > 2 or alertness < 0.6 or hypertension > 0.6 or intoxication > 0.2:
        return 3  # Sleep
    
    # Optimized coffee usage when alertness is moderate
    if alertness < 0.75 and hypertension <= 0.3 and intoxication <= 0.1:
        return 1  # Drink coffee and work
    
    # Strong healthy condition for working
    if alertness >= 0.8 and hypertension <= 0.3 and intoxication <= 0.1:
        return 0  # Just work
    
    # Avoid beer to maintain better health balance
    return 0  # Default action is just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
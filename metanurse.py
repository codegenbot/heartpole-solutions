import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Key conditions for prioritizing health
    if alertness < 0.5 or hypertension > 0.2 or intoxication > 0.1 or time_since_slept > 8:
        return 3  # Sleep
    
    # Drink coffee to boost alertness only if health is stable and alertness is low
    if alertness >= 0.5 and alertness < 0.7 and hypertension <= 0.15 and intoxication <= 0.05:
        return 1  # Drink coffee and work
    
    # Avoid beer unless all other parameters are very stable
    if intoxication < 0.05 and alertness >= 0.6 and hypertension <= 0.1:
        return 2  # Drink beer and work

    # Default to working if all parameters are stable
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if alertness is low and sleep deprivation is significant
    if alertness < 0.5 or time_since_slept > 6:
        return 3
    
    # Use coffee sparingly to boost alertness without impacting health negatively
    if alertness < 0.7 and hypertension < 0.15 and intoxication < 0.05:
        return 1
    
    # Avoid beer; only use if minimally intoxicated and alertness is critically low
    if alertness < 0.3 and intoxication < 0.03:
        return 2
    
    # Work if alertness is sufficient and health metrics are balanced
    if alertness >= 0.5 and hypertension < 0.25 and intoxication < 0.1:
        return 0
    
    # Default to working if no action is triggered
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
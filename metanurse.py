import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate critical conditions warranting sleep
    if hypertension > 0.7 or intoxication > 0.5 or alertness < 0.2 or time_since_slept > 16:
        return 3
    
    # Work directly under ideal conditions
    if alertness >= 0.8 and hypertension <= 0.3 and intoxication == 0.0:
        return 0
    
    # Increase caution with sleep for moderately low alertness
    if alertness < 0.35 or time_since_slept > 12:
        return 3
    
    # Use coffee cautiously to boost alertness, avoiding hypertension
    if alertness < 0.5 and hypertension <= 0.4:
        return 1
    
    # Default to work if no adverse conditions
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
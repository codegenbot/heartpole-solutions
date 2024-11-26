import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if any health metric is critically high or if severe sleep deprivation
    if hypertension > 0.015 or intoxication > 0.05 or alertness < 0.4 or time_since_slept > 6:
        return 3
    
    # If moderately low alertness and health metrics are within moderate range
    if 0.4 <= alertness < 0.5 and hypertension < 0.01 and intoxication < 0.03:
        return 1
    
    # Use beer for productivity boost with safer parameters and less frequency
    if time_elapsed >= 300 and time_elapsed % 200 == 0 and hypertension < 0.008 and intoxication < 0.015:
        return 2
    
    # Default to just work for moderate alertness and stable health
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
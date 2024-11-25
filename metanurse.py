import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if alertness is low or time since last slept is high
    if alertness < 0.5 or time_since_slept > 6:
        return 3
    
    # Sleep immediately if hypertension or intoxication are critically high
    if hypertension >= 0.12 or intoxication >= 0.1:
        return 3
    
    # Use coffee only if alertness is low without significant hypertension or intoxication
    if alertness < 0.6 and hypertension <= 0.08 and intoxication <= 0.03:
        return 1
        
    # Work normally if alertness is reasonably high and health parameters are normal
    if alertness >= 0.65 and hypertension <= 0.07 and intoxication <= 0.02:
        return 0

    # Avoid beer unless health is stable and more work is needed
    if alertness > 0.55 and work_done < 0.03 and hypertension <= 0.05 and intoxication <= 0.02:
        return 2

    # Default to safe working condition
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
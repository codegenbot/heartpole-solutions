import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if alertness is low, time since sleep or time elapsed is high, or hypertension is high
    if alertness < 0.4 or time_since_slept >= 4 or hypertension > 0.1 or time_elapsed > 8:
        return 3
    
    # Use coffee carefully to boost alertness only if it won't elevate hypertension
    if 0.4 <= alertness < 0.6 and hypertension <= 0.03 and intoxication < 0.03:
        return 1
    
    # Continue working if alertness is high and health indicators are very low
    if alertness >= 0.6 and hypertension < 0.02 and intoxication < 0.01:
        return 0
    
    # Default to work if no critical health flags, prioritizing health over maximum work speed
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
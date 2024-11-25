import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if alertness is low or time since sleep is high
    if alertness < 0.3 or time_since_slept >= 5 or hypertension > 0.12:
        return 3
    
    # Drink coffee to boost alertness if moderately low
    if 0.3 <= alertness < 0.5 and hypertension < 0.04 and intoxication < 0.05:
        return 1
    
    # Continue working if alertness is high and health indicators are low
    if alertness >= 0.5 and hypertension < 0.03 and intoxication < 0.02:
        return 0

    # Use beer sparingly when work done is very low and alertness is critically low
    if work_done < 0.05 and intoxication <= 0.01 and alertness < 0.25:
        return 2
    
    # Default to work if no critical health flags
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Always prioritize sleep if health issues are detected
    if alertness < 0.4 or hypertension > 0.15 or intoxication > 0.1 or time_since_slept > 8:
        return 3
    
    # Use coffee to combat low alertness but ensure it's safe
    if alertness < 0.5 and hypertension < 0.1 and intoxication < 0.03 and time_since_slept < 6:
        return 1
        
    # Allow work if alertness is sufficient and health stats are under control
    if alertness >= 0.5 and hypertension <= 0.1 and intoxication <= 0.03:
        return 0
    
    # Use beer cautiously when productivity is very low and conditions are safe
    if work_done < 0.15 and alertness > 0.5 and hypertension < 0.08 and intoxication < 0.02:
        return 2

    # Default action if none of the above are met
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
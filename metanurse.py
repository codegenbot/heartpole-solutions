import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep if any health issue is above threshold
    if hypertension > 0.5 or intoxication > 0.3:
        return 3
    
    # Sleep if alertness is critically low
    if alertness < 0.4:
        return 3
    
    # Early coffee usage when it is likely to be most effective, but avoid later
    if time_elapsed < 8 and alertness < 0.55 and work_done < 0.3:
        return 1
    
    # Preserve health during late day or low alertness
    if alertness < 0.45:
        return 3

    # Default action is work if health parameters are safe
    return 0 if (alertness > 0.5 and hypertension <= 0.2 and intoxication <= 0.15) else 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
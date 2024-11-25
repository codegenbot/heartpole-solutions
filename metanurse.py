import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Always prioritize sleep if health issues are detected
    if alertness < 0.45 or hypertension > 0.12 or intoxication > 0.08 or time_since_slept > 6:
        return 3
    
    # Use coffee if slightly low alertness, consider hypertension limit
    if alertness < 0.55 and hypertension < 0.09 and intoxication < 0.03 and time_since_slept < 6:
        return 1
        
    # Allow work if sufficient alertness and health stats are optimal
    if alertness >= 0.6 and hypertension <= 0.08 and intoxication <= 0.02:
        return 0
    
    # Rarely use beer with tight constraints for when productivity is very low
    if work_done < 0.1 and alertness > 0.55 and hypertension < 0.06 and intoxication < 0.01:
        return 2

    # Default action if none of the above are met
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
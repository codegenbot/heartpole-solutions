import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for critical health issues
    if hypertension > 0.6 or intoxication > 0.4:
        return 3
    
    # Opt to sleep if time awake is lengthy or alertness is low
    if time_since_slept > 10 or alertness < 0.3:
        return 3
    
    # Use coffee to boost alertness under safe conditions
    if alertness < 0.7 and hypertension <= 0.25 and intoxication <= 0.2 and work_done < 0.6:
        return 1
    
    # Work if conditions suggest safe operation
    if alertness >= 0.6 and hypertension <= 0.15 and intoxication <= 0.1:
        return 0
    
    # Opt for sleep over work in the evening with low alertness
    if time_elapsed >= 16 and alertness < 0.5:
        return 3

    # Default to work if alertness is decent
    return 0 if alertness > 0.5 else 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
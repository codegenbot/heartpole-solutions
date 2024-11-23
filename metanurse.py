import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize health issues
    if hypertension > 0.5 or intoxication > 0.4:
        return 3  # Sleep to alleviate health issues
    
    # Optimize alertness and productivity
    if alertness < 0.4 and time_since_slept > 7:
        return 3  # Sleep if alertness is low and awake time is significant
    if alertness < 0.6:
        if time_elapsed < 10:
            return 1  # Drink coffee during active work hours
        return 3  # Sleep when it's late and alertness is low
    
    # Encourage sleep if awake for too long
    if time_since_slept > 10:
        return 3
    
    # Encourage work if alertness is high and work done is low
    if work_done < 0.7 and alertness > 0.7:
        return 0
    
    # Default to just work if everything seems optimal
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
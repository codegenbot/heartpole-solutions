import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if time_since_slept > 10 or alertness < 0.4 or hypertension > 0.6 or intoxication > 0.5:
        return 3  # Prioritize sleep for recovery if conditions are critical
    
    if alertness < 0.7:
        if hypertension < 0.5 and intoxication < 0.3:
            return 1  # Drink coffee and work if safe
    
    if alertness >= 0.7 and hypertension < 0.4 and intoxication < 0.4:
        return 0  # Just work when conditions are quite good
    
    return 2  # Default to drink beer and work if no conditions of sleep or coffee are met

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
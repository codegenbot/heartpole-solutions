import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep if any serious condition is met
    if alertness < 0.3 or hypertension > 0.7 or intoxication > 0.6 or time_since_slept > 10:
        return 3
    
    # Drink coffee and work if moderate alertness and manageable health metrics
    if alertness < 0.6 and hypertension <= 0.5 and intoxication < 0.4:
        return 1
    
    # Just work if alertness is high and health indicators are stable
    if alertness >= 0.7 and hypertension < 0.4 and intoxication < 0.3:
        return 0
    
    # Drink beer and work if light intoxication is manageable and recent sleep
    if intoxication < 0.5 and hypertension <= 0.5 and 4 <= time_since_slept <= 9:
        return 2

    # Default action if decision criteria aren't strong
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
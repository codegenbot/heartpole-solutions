import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize health: sleep if any severe conditions
    if alertness < 0.4 or hypertension > 0.3 or intoxication > 0.25 or time_since_slept > 8:
        return 3
    
    # Drink coffee if alertness is low but other health indicators are acceptable
    if alertness < 0.6 and hypertension < 0.15 and intoxication < 0.1 and time_since_slept <= 6:
        return 1
    
    # If alertness and health are fine, prioritize just working
    if alertness >= 0.7 and hypertension <= 0.15 and intoxication < 0.1:
        return 0
    
    # Drink beer if doing fine and more relaxing boost is needed
    if alertness > 0.75 and hypertension < 0.15 and intoxication < 0.05 and work_done < 0.5:
        return 2

    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
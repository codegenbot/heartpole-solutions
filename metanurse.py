import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # High health risk; must sleep
    if hypertension > 0.7 or intoxication > 0.5:
        return 3
    
    # Adequate sleep strategy based on alertness and time since slept
    if alertness < 0.4 or time_since_slept > 7:
        return 3
    
    # Drink coffee if alertness is low but health parameters are safe
    if 0.4 <= alertness < 0.6 and hypertension <= 0.5 and intoxication < 0.2:
        return 1
    
    # Continue working if sufficient alertness and healthy condition
    if alertness >= 0.6 and hypertension <= 0.5 and intoxication < 0.3:
        return 0
    
    # Consume beer if mild intoxication and safe hypertension level
    if 0.2 <= intoxication < 0.4 and hypertension <= 0.5:
        return 2
    
    # Default to sleep as a conservative health action
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
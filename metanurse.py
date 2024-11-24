import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.75 or intoxication > 0.4:
        return 3  # Sleep
    
    if time_since_slept >= 5 or alertness < 0.55:
        return 3  # Sleep
    
    if alertness < 0.65 and hypertension <= 0.3:
        return 1  # Drink coffee and work
    
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
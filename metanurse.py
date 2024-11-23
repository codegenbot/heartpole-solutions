import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 8 or alertness < 0.5 or hypertension > 0.12 or intoxication > 0.07:
        return 3  # Sleep
    
    if alertness < 0.7 and hypertension <= 0.08 and intoxication <= 0.04:
        return 1  # Drink coffee and work
    
    if alertness >= 0.9 and hypertension < 0.03 and intoxication < 0.02:
        return 2  # Drink beer and work
    
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
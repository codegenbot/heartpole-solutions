import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 5.5 or hypertension > 0.5 or alertness < 0.3:
        return 3  # Sleep to restore alertness and health balance
    if alertness > 0.7 and hypertension < 0.3 and intoxication == 0.0:
        return 0  # Work when alert and healthy
    if alertness < 0.5 and intoxication < 0.1:
        return 1  # Need a boost, so drink coffee and work if not too intoxicated
    if alertness < 0.5 and hypertension < 0.25:
        return 2  # Drink beer only if slightly intoxicated and low hypertension
    
    return 0  # Default action to just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
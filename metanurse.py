import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if hypertension or intoxication is dangerously high
    if hypertension > 0.6 or intoxication > 0.4:
        return 3
    
    # Increase the need for sleep with lower alertness or excessive awake time
    if alertness < 0.4 or time_since_slept > 8:
        return 3
    
    # Use coffee to boost productivity when conditions are moderate
    if alertness < 0.5 and hypertension <= 0.5 and intoxication < 0.2:
        return 1
    
    # If both alertness and hypertension are optimal, just work
    if alertness >= 0.5 and hypertension < 0.4 and intoxication < 0.3:
        return 0
    
    # Beer used to mitigate moderate intoxication when neither health nor productivity is compromised
    if intoxication >= 0.2 and hypertension < 0.5:
        return 2
    
    # Default to sleep if no other condition above applies
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
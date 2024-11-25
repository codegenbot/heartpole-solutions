import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep for health risks: hypertension, intoxication, alertness, or long awake time
    if hypertension > 0.2 or intoxication > 0.1 or alertness < 0.4 or time_since_slept >= 6:
        return 3
    
    # Use coffee to boost if under threshold conditions
    if alertness < 0.6 and hypertension <= 0.1 and intoxication < 0.05:
        return 1
    
    # Safely allow work with sufficient alertness and minimal health risk
    if alertness >= 0.7 and hypertension < 0.1 and intoxication < 0.05:
        return 0
    
    # Minimize beer usage due to negative health impact
    if alertness >= 0.6 and hypertension < 0.1 and intoxication < 0.1:
        return 2

    # Default to working if conditions are neutral
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
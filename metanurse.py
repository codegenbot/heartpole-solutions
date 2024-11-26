import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep takes precedence when needed for hypertension or intoxication
    if hypertension > 0.025 or intoxication > 0.12:
        return 3  # sleep to address health risks
    
    # Further sleep conditions for recovery and alertness
    if time_since_slept >= 7 or alertness < 0.25:
        return 3  # sleep to recover from lack of sleep or low alertness   
    
    # Drink coffee to boost alertness if within safe health parameters
    if alertness < 0.7 and hypertension < 0.02 and intoxication < 0.08:
        return 1  # use coffee to improve productivity
    
    # Manage moderate intoxication with beer
    if 0.06 < intoxication < 0.09 and hypertension < 0.01:
        return 2  # use beer to manage intoxication within safe limits
    
    # Default to working when conditions are optimal
    return 0  # just work otherwise

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
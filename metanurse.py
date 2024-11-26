import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep takes precedence when needed for hypertension or intoxication
    if hypertension > 0.03 or intoxication > 0.15:
        return 3  # sleep to address serious health risks
    
    # Further sleep conditions for recovery and alertness
    if time_since_slept >= 8 or alertness < 0.2:
        return 3  # sleep to recover from lack of sleep or very low alertness   
    
    # Drink coffee to boost alertness if health parameters are in acceptable range
    if alertness < 0.5 and hypertension < 0.02 and intoxication < 0.12:
        return 1  # use coffee to maintain productivity
    
    # Moderate intoxication management with beer balancing between risk and work
    if intoxication > 0.06 and hypertension < 0.01:
        return 2  # use beer to manage intoxication if not too risky
    
    # Default to working when none of the above conditions apply
    return 0  # just work otherwise

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
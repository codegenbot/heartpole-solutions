def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Always prioritize sleep if health is at risk
    if alertness < 0.5 or hypertension > 0.1 or intoxication > 0.07 or time_since_slept > 5.5:
        return 3
    
    # Use coffee more often for low alertness but safe health stats
    if alertness < 0.6 and hypertension < 0.09 and intoxication <= 0.02:
        return 1
        
    # Work if alertness and health are optimal
    if alertness >= 0.6 and hypertension <= 0.08 and intoxication <= 0.02:
        return 0

    # Reduce the likelihood of using beer
    if work_done < 0.08 and alertness > 0.55 and hypertension < 0.05 and intoxication < 0.01:
        return 2

    # Default action if none of the above conditions is met
    return 0

# Read from stdin and process each line
import sys

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
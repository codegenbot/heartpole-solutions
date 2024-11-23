import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep conditions prioritizing critical health levels
    if alertness < 0.3 or hypertension > 0.7 or intoxication > 0.6 or time_since_slept > 8:
        return 3  # Sleep is prioritized for recovery
    
    # Coffee strategy for boosting alertness without risking hypertension
    if 0.3 <= alertness < 0.5 and hypertension < 0.15:
        return 1  # Coffee to increase alertness safely

    # Optimal work condition
    if alertness >= 0.5 and hypertension < 0.2 and intoxication < 0.1:
        return 0  # Work in good condition

    # Use work to reduce reliance on beer
    return 0  # Default action is to work focusing on productivity

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.4 or time_since_slept > 8 or intoxication > 0.1:
        return 3  # Sleep if too tired, intoxicated, or not rested
    
    if alertness < 0.6 and hypertension < 0.04 and intoxication < 0.05:
        return 1  # Coffee to improve alertness when it's moderate and health permits
    
    if intoxication < 0.02 and work_done < 0.1 and alertness < 0.5:
        return 2  # Beer in case work is minimal and alertness is low but safe

    return 0  # Default to working when conditions are suitable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Strongly encourage sleep when moderately deprived
    if alertness < 0.3 or intoxication > 0.15 or time_since_slept >= 6.5:
        return 3
    
    # Use coffee with more guarded conditions
    if alertness < 0.6 and hypertension < 0.035 and intoxication <= 0.04:
        return 1

    # Safe zone for work with stricter health checks
    if alertness >= 0.65 and hypertension < 0.03 and intoxication < 0.025:
        return 0

    # More conservative use of beer with better conditions
    if work_done < 0.02 and intoxication <= 0.01 and alertness < 0.4:
        return 2
    
    # Default to work if no other conditions are met, keeping safety in mind
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
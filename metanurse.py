import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Encourage sleep when it's needed
    if alertness < 0.3 or intoxication > 0.15 or time_since_slept >= 6:
        return 3
    
    # Use coffee wisely
    if 0.4 < alertness < 0.55 and hypertension < 0.05 and intoxication < 0.05:
        return 1

    # Continue work if in good conditions
    if alertness >= 0.6 and hypertension < 0.04 and intoxication < 0.04:
        return 0
    
    # Conservative beer use if low conditions
    if work_done < 0.02 and intoxication <= 0.02 and alertness < 0.3:
        return 2
    
    # Default to work
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
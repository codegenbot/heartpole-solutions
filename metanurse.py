import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Critical or poor health condition
    if hypertension > 0.03 or intoxication > 0.07 or alertness < 0.5:
        return 3
    
    # Ensure regular rest
    if time_since_slept > 6.0:
        return 3
    
    # Strategic coffee use for boosting alertness
    if alertness < 0.7 and hypertension < 0.025 and intoxication < 0.03:
        return 1

    # Use beer when critical and safe
    if alertness < 0.6 and intoxication < 0.03 and hypertension < 0.02:
        return 2

    # Work when in high alert and low health risks
    if alertness >= 0.75 and hypertension < 0.015 and intoxication < 0.015:
        return 0

    return 3  # Default to rest for safe recovery

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
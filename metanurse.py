import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if severely lacking alertness or too long without sleep
    if alertness < 0.2 or time_since_slept >= 8 or (hypertension >= 0.8 and intoxication > 0.3):
        return 3
    
    # Improve alertness with coffee if safe
    if alertness < 0.5 and hypertension < 0.6:
        return 1
    
    # Work directly if alertness is good and health is stable
    if alertness >= 0.7 and hypertension < 0.6 and intoxication <= 0.1:
        return 0
    
    # Default to work if no other condition is critical
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
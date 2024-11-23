import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Tighten sleep criteria for recovery
    if alertness < 0.5 or hypertension > 0.55 or intoxication > 0.4 or time_since_slept > 8:
        return 3  # Sleep for better recovery
    
    # Adjust coffee use, only when alertness is moderate and health is stable
    if 0.5 <= alertness < 0.65 and hypertension < 0.2 and intoxication < 0.2:
        return 1  # Use coffee if conditions favor alertness
    
    # Stricter criteria for working
    if alertness >= 0.65 and hypertension < 0.3 and intoxication < 0.2:
        return 0  # Work optimally by ensuring stable health
    
    # Use beer cautiously for moderate hypertension relief
    if 0.35 <= hypertension < 0.45 and intoxication < 0.15:
        return 2  # Reduce stress with little risk of intoxication

    # Default to safer action of working when unsure but healthy
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
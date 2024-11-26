import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep when critical health alerts are detected
    if hypertension > 0.02 or intoxication > 0.08:
        return 3
    
    # Sleep if not slept for a while or alertness is notably low
    if time_since_slept > 4 or alertness < 0.5:
        return 3
    
    # Coffee if under alertness threshold and health within safer limits
    if alertness < 0.65 and hypertension < 0.015 and intoxication < 0.03:
        return 1
    
    # Default to working if everything is stable
    if alertness >= 0.7 and hypertension < 0.01:
        return 0

    return 0  # Ensure safe fallback to working

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
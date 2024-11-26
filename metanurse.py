import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for high-risk health indicators
    if hypertension > 0.02 or intoxication > 0.07:
        return 3
    
    # Sleep if sleep-deprived or alertness is below threshold
    if time_since_slept > 2.5 or alertness < 0.5:
        return 3
    
    # Use coffee cautiously to boost productivity if alertness is slightly low and health is stable
    if alertness < 0.55 and hypertension < 0.015 and intoxication < 0.02 and work_done < 0.8:
        return 1

    # Default to working if conditions are generally favorable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
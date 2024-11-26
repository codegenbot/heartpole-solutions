import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for high-risk health indicators
    if hypertension > 0.02 or intoxication > 0.07:
        return 3
    
    # Sleep if severely sleep deprived or very low alertness
    if time_since_slept > 3 or alertness < 0.4:
        return 3
    
    # Use coffee to boost productivity if slightly low alertness and health is stable
    if alertness < 0.55 and hypertension < 0.015 and intoxication < 0.03:
        return 1

    # Use beer occasionally to reduce stress if health is very stable
    if (time_elapsed % 150 == 0) and hypertension < 0.01 and intoxication < 0.02:
        return 2

    # Default to working if all conditions are generally favorable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
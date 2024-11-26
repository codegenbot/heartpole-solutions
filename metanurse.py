import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if essential
    if alertness < 0.6 or time_since_slept > 10.0:
        return 3
    
    # Avoid severe hypertension and intoxication
    if hypertension > 0.07 or intoxication > 0.07:
        return 3
    
    # Use coffee for alertness boost when healthy
    if alertness < 0.8 and hypertension <= 0.04:
        return 1
    
    # Allow limited use of beer if alertness is high and intoxication very low
    if alertness >= 0.8 and intoxication < 0.01:
        return 2

    # Default to working
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
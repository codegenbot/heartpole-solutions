import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if essential
    if alertness < 0.5 or time_since_slept > 8.0:
        return 3
    
    # Avoid severe health risks
    if hypertension > 0.05 or intoxication > 0.05:
        return 3
    
    # Use coffee for moderate alertness boost
    if 0.5 <= alertness < 0.7 and hypertension <= 0.03:
        return 1

    # Avoid beer unless sure about low intoxication needs (not encouraged)
    if alertness >= 0.7 and intoxication <= 0.02:
        return 2

    # Default to working
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
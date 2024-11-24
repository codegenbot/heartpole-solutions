import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep to avoid severe health risks
    if (
        alertness < 0.5
        or hypertension > 0.75
        or intoxication > 0.4
        or time_since_slept > 8
    ):
        return 3
    
    # Avoid caffeine if hypertension is high despite low alertness
    if (
        alertness < 0.7
        and hypertension < 0.65
        and intoxication < 0.25
        and time_since_slept <= 8
    ):
        return 1

    # Favor work if generally healthy
    if alertness >= 0.7 and hypertension < 0.65 and intoxication < 0.2:
        return 0
    
    # Use beer cautiously
    if hypertension < 0.7 and 0.3 <= intoxication < 0.45:
        return 2

    # Default back to just work as a safer option
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
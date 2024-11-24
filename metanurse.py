import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Always prioritize sleep for severe health risks
    if alertness < 0.6 or hypertension >= 0.8 or intoxication >= 0.5 or time_since_slept > 7:
        return 3

    # Use coffee cautiously when slightly tired but under safe conditions
    if alertness < 0.8 and hypertension < 0.7 and intoxication < 0.3 and time_since_slept <= 7:
        return 1

    # Keep working if all parameters are within healthy limits
    if alertness >= 0.8 and hypertension < 0.7 and intoxication < 0.2:
        return 0

    # Reduce use of beer, very limited conditions to use
    if 0.3 <= intoxication < 0.4 and hypertension < 0.7:
        return 2

    # Safe default to work if conditions are ambiguous
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
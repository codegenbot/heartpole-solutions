import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if hypertension or intoxication is too high
    if hypertension > 0.03 or intoxication > 0.08:
        return 3

    # Sleep if very low alertness, or overdue for sleep
    if alertness < 0.5 or time_since_slept > 7:
        return 3

    # Use beer to moderate hypertension with criteria slightly adjusted for safety
    if 0.02 < hypertension <= 0.03 and intoxication < 0.03 and alertness > 0.7:
        return 2

    # Use coffee strategically when alertness is declining and health allows
    if alertness < 0.7 and hypertension < 0.02 and intoxication < 0.03:
        return 1

    # Default to work if no immediate health risks
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
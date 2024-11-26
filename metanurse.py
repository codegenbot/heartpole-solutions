import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if hypertension or intoxication is too high
    if hypertension > 0.03 or intoxication > 0.08:
        return 3

    # Sleep if very low alertness (before it gets too risky)
    if alertness < 0.5 or time_since_slept > 5:
        return 3

    # Use beer for moderate hypertension given low intoxication and sufficient alertness
    if 0.02 < hypertension <= 0.03 and intoxication < 0.05 and alertness > 0.7:
        return 2

    # Coffee if alertness is low and health is stable, but prioritize avoiding risk
    if alertness < 0.6 and hypertension < 0.02 and intoxication < 0.03:
        return 1

    # Default work if no health risks
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
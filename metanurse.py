import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if hypertension or intoxication is concerning
    if hypertension > 0.02 or intoxication > 0.06:
        return 3

    # Sleep if alertness falls or if it’s been too long since last slept
    if alertness < 0.6 or time_since_slept > 4:
        return 3

    # Coffee with a safer margin, combining alertness boost with low health risk
    if alertness < 0.7 and hypertension < 0.015 and intoxication < 0.02:
        return 1

    # Consider beer when hypertension is slightly high but with good alertness and low intoxication
    if 0.015 < hypertension <= 0.02 and intoxication < 0.04 and alertness > 0.75:
        return 2

    # Default work if no immediate health risk
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
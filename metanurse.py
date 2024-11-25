import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep for poor conditions or lack of recent sleep
    if hypertension > 0.12 or intoxication > 0.05 or alertness < 0.5 or time_since_slept >= 6:
        return 3
    # Drink coffee to maintain good alertness if within safe hypertension and intoxication limits
    if alertness < 0.75 and hypertension < 0.07 and intoxication < 0.03:
        return 1
    # Allow working with beer if moderate alertness and within reasonable intoxication levels
    if alertness < 0.7 and hypertension < 0.06 and intoxication < 0.04:
        return 2
    # Default to just working if conditions are optimal
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
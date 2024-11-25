import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep on poor conditions
    if alertness < 0.4 or hypertension > 0.7 or intoxication > 0.3 or time_since_slept > 8:
        return 3  # Need sleep

    # Productive conditions: prioritize work
    if alertness > 0.85 and hypertension < 0.45 and intoxication < 0.1:
        return 0  # Just work

    # Moderate alertness: carefully use coffee
    if 0.6 <= alertness < 0.85 and hypertension < 0.6 and intoxication < 0.1:
        return 1  # Coffee and work

    # Default action when conditions are not optimal for work
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
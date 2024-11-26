import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep for high-risk health indicators
    if hypertension > 0.015 or intoxication > 0.03:
        return 3
    
    # Optimize sleep and alertness conditions
    if alertness < 0.6 or time_since_slept > 3:
        return 3

    # Increase coffee usage when health allows
    if alertness < 0.7 and hypertension < 0.01 and intoxication < 0.02:
        return 1

    # Default action if conditions are stable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
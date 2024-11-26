import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # High-risk health indicators: prioritize sleep
    if hypertension > 0.02 or intoxication > 0.05:
        return 3
    
    # Improved sleep condition
    if alertness < 0.5 or time_since_slept > 3:
        return 3

    # Use coffee wisely to balance alertness and health
    if alertness < 0.6 and hypertension < 0.015 and intoxication < 0.03:
        return 1

    # Avoid excessive beer use
    if 0.5 <= alertness <= 0.75 and 0.015 < hypertension <= 0.02 and intoxication < 0.03:
        return 2

    # Default action if conditions are stable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
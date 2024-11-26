import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # High-risk health indicators: prioritize sleep
    if hypertension > 0.03 or intoxication > 0.08:
        return 3
    
    # Improved sleep condition
    if alertness < 0.6 or time_since_slept > 4:
        return 3

    # Use coffee wisely to balance alertness and health
    if alertness < 0.7 and hypertension < 0.02 and intoxication < 0.04:
        return 1

    # Be selective with beer usage to avoid intoxication buildup
    if 0.6 <= alertness <= 0.8 and 0.02 < hypertension <= 0.03 and intoxication < 0.04:
        return 2

    # Default action if conditions are stable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
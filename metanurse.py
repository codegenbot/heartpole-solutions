import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if any health parameter is critical
    if hypertension > 0.75 or intoxication > 0.5 or time_since_slept > 8:
        return 3
    # Sleep if alertness is critically low
    if alertness < 0.4:
        return 3
    # Drink coffee if alertness is low but other health parameters are safe
    if alertness < 0.6 and hypertension < 0.7 and intoxication < 0.3:
        return 1
    # Just work if all conditions are optimal or safe
    if alertness >= 0.75 and hypertension < 0.5 and intoxication < 0.2:
        return 0
    # Use beer to diminish health impact when it seems appropriate
    if hypertension < 0.7 and intoxication < 0.5:
        return 2
    # Default to sleep as a conservative approach
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
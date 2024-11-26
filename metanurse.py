import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Lower health thresholds for safety
    if hypertension > 0.012 or intoxication > 0.035:
        return 3

    # Sleep if alertness is moderate or haven't slept in a while
    if time_since_slept > 5 or alertness < 0.5:
        return 3
    
    # Use coffee if moderately alert and health are stable
    if 0.5 <= alertness < 0.8 and hypertension < 0.01 and intoxication < 0.02:
        return 1
    
    # Use beer for quick breaks if right circumstances
    if 0.8 <= alertness < 0.9 and hypertension < 0.006 and intoxication < 0.01:
        return 2
    
    # Regular work if conditions are optimal
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
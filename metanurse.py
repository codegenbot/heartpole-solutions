import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep if not slept recently or if intoxication is high
    if time_since_slept > 8 or alertness < 0.5 or intoxication > 0.2:
        return 3
    
    # Boost with coffee if alertness is moderate and hypertension is low
    if alertness < 0.65 and hypertension < 0.05:
        return 1
    
    # Work if alertness and health indicators are in good range
    if alertness >= 0.75 and hypertension <= 0.03 and intoxication <= 0.1:
        return 0
    
    # Use beer sparingly and only with low work_done and intoxication under control
    if work_done < 0.2 and intoxication <= 0.05:
        return 2
    
    # Use work as a default when conditions do not strongly favor other actions
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
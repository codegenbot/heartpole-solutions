import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep when fatigue is high
    if time_since_slept > 6 or alertness < 0.4 or intoxication > 0.1:
        return 3
    
    # Boost with coffee when mildly tired but health is okay
    if alertness < 0.6 and hypertension < 0.07:
        return 1
    
    # Optimal conditions to just work
    if alertness >= 0.7 and hypertension < 0.03 and intoxication <= 0.02:
        return 0
    
    # Avoid beer unless work_done is very low and minimal intoxication
    if work_done < 0.1 and intoxication <= 0.05:
        return 2

    # Default to just work as last resort
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
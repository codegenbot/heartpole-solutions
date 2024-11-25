import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.12 or intoxication > 0.10 or time_since_slept > 6:
        return 3  # sleep if any significant health issues
    
    if alertness < 0.5:
        return 3  # sleep to boost low alertness quickly
    
    if alertness < 0.7:
        if hypertension < 0.1:
            return 1  # use coffee to increase alertness if safely possible
    
    if alertness >= 0.7 and hypertension < 0.08 and intoxication < 0.04:
        return 0  # just work if conditions are optimal
    
    if work_done < 0.3 and alertness > 0.55:
        if intoxication < 0.1:
            return 2  # moderate relaxation with beer and work

    return 0  # default to just working if no other actions are prioritized

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
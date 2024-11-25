import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep when alertness is low, long without sleep, or high intoxication
    if time_since_slept > 5 or alertness < 0.4 or intoxication > 0.1:
        return 3
    
    # Drink coffee to boost alertness sparingly when it is moderately low and health markers are stable
    if alertness < 0.6 and hypertension < 0.07 and intoxication <= 0.05:
        return 1
    
    # Optimal to work if high alertness and stable health
    if alertness >= 0.8 and hypertension < 0.05 and intoxication < 0.04:
        return 0
    
    # Drink beer carefully for relaxation when alertness is very low and safe intoxication levels
    if work_done < 0.02 and intoxication <= 0.02 and alertness < 0.3:
        return 2

    # Default to just work conservatively when other conditions don't fit
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
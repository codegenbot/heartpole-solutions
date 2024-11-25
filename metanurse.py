import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Encourage sleep when alertness is critically low or too long without sleep
    if time_since_slept > 8 or alertness < 0.3 or intoxication > 0.15:
        return 3
    
    # Use coffee if alertness is average and health markers are stable
    if alertness < 0.5 and hypertension < 0.05 and intoxication <= 0.05:
        return 1
    
    # Optimal to work if good alertness and health conditions
    if alertness >= 0.65 and hypertension < 0.03 and intoxication < 0.03:
        return 0
    
    # Beer only in rare cases when work_done is zero or negligible and health allows
    if work_done < 0.05 and intoxication <= 0.02 and alertness < 0.4:
        return 2

    # Default to work conservatively when other conditions don't fit
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
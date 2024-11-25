import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep when alertness is low or long without sleep
    if time_since_slept > 6 or alertness < 0.4 or intoxication > 0.2:
        return 3
    
    # Use coffee sparingly when alertness is moderately low and health markers are stable
    if alertness < 0.6 and hypertension < 0.05 and intoxication <= 0.05:
        return 1
    
    # Optimal to work if high alertness and good health
    if alertness >= 0.7 and hypertension < 0.04 and intoxication < 0.03:
        return 0
    
    # Rarely use beer only when no work is done, alertness is very low, but low intoxication
    if work_done < 0.02 and intoxication <= 0.02 and alertness < 0.35:
        return 2

    # Default to just work conservatively when other conditions don't fit
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
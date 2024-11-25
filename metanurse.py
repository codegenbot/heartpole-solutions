import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep if alertness is critically low or health signals are problematic
    if alertness < 0.3 or hypertension > 0.15 or intoxication > 0.1 or time_since_slept >= 5:
        return 3
    
    # Use coffee wisely when alertness is moderately low, but health conditions are stable
    if 0.35 <= alertness < 0.5 and hypertension < 0.05 and intoxication < 0.05:
        return 1
    
    # Continue work if in good conditions
    if alertness >= 0.5 and hypertension < 0.04 and intoxication < 0.04:
        return 0

    # Avoid beer unless it's strategically timed for very low work conditions AND safe health
    if work_done < 0.08 and intoxication <= 0.02 and alertness < 0.3:
        return 2

    # Default to work
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for any significant health issues
    if hypertension > 0.6 or intoxication > 0.4:
        return 3
    
    # Opt to sleep if time awake is excessive or alertness is critically low
    if time_since_slept > 12 or alertness < 0.3:
        return 3
    
    # Use coffee to boost alertness in early cases of depletion
    if alertness < 0.6 and time_elapsed < 10 and work_done < 0.5:
        return 1
    
    # Use beer as a productivity booster when not at high risk
    if intoxication <= 0.15 and work_done < 0.7 and alertness > 0.5:
        return 2
    
    # Work normally if metrics are healthy and there's capability to do so
    if alertness >= 0.6 and hypertension <= 0.25 and intoxication <= 0.2:
        return 0
    
    # Prioritize sleep in the afternoon as alertness dwindles
    if time_elapsed >= 14 and alertness < 0.5:
        return 3

    # Default to work if moderate alertness is maintained
    return 0 if alertness > 0.5 else 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
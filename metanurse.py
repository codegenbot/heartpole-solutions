import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Critical health concern management
    if alertness < 0.4 or hypertension > 0.08 or intoxication > 0.05 or time_since_slept >= 3.0:
        return 3  # Sleep if any health indicators are poor.
    
    # Use coffee if alertness is medium and hypertension is low
    if 0.5 <= alertness < 0.7 and hypertension < 0.04:
        return 1  # Coffee if small productivity boost is needed.
    
    # Work optimally when fully alert and health is good
    if alertness >= 0.7 and hypertension < 0.03 and intoxication < 0.01:
        return 0  # Work if all health and alertness indicators are optimal.
    
    # Default to just working if conditions are moderately good and do not pose a risk
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
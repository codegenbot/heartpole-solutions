import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for high-risk levels
    if hypertension > 0.02 or intoxication > 0.07:
        return 3
    
    # Sleep based on sleep deprivation or severe drop in alertness
    if time_since_slept > 4 or alertness < 0.35:
        return 3
    
    # Use coffee when alertness is low but health indicators are stable
    if alertness < 0.45 and hypertension < 0.015 and intoxication < 0.04:
        return 1

    # Use beer to reduce stress under very controlled conditions
    if time_elapsed % 100 == 0 and hypertension < 0.015 and intoxication < 0.03:
        return 2

    # Work by default if health indicators are stable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
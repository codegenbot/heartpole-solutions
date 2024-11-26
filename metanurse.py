import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for high-risk levels
    if hypertension > 0.03 or intoxication > 0.1:
        return 3
    
    # Sleep based on sleep deprivation or severe drop in alertness
    if time_since_slept > 5 or alertness < 0.4:
        return 3
    
    # Use coffee when alertness is low but health is not in danger
    if alertness < 0.5 and hypertension < 0.02 and intoxication < 0.05:
        return 1

    # Use beer to reduce stress under safer conditions
    if time_elapsed % 100 == 0 and hypertension < 0.02:
        return 2

    # Work by default if health indicators are stable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
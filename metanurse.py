import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for high-risk levels
    if hypertension > 0.015 or intoxication > 0.06:
        return 3
    
    # Sleep based on sleep deprivation or significant drop in alertness
    if time_since_slept > 3.5 or alertness < 0.40:
        return 3
    
    # Use coffee when alertness is moderately low and risk factors are in check
    if alertness < 0.50 and hypertension < 0.012 and intoxication < 0.035:
        return 1

    # Use beer under very controlled conditions for stress relief if needed
    if time_elapsed % 200 == 0 and hypertension < 0.012 and intoxication < 0.025:
        return 2

    # Work by default if health indicators are stable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
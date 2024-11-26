import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if health is dangerously compromised
    if hypertension > 0.03 or intoxication > 0.08:
        return 3
    
    # Prioritize sleep for significant sleep deprivation or very low alertness
    if time_since_slept > 6 or alertness < 0.4:
        return 3
    
    # Boost alertness if it's moderately low and health indicators are stable
    if 0.4 <= alertness < 0.7 and hypertension < 0.02 and intoxication < 0.04:
        return 1

    # Use beer sparingly only under stricter health conditions
    if time_elapsed > 300 and time_elapsed % 200 == 0 and hypertension < 0.015 and intoxication < 0.025:
        return 2
    
    # Regular work for all other stable conditions
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
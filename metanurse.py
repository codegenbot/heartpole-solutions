import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if health is critically compromised
    if hypertension > 0.02 or intoxication > 0.06:
        return 3
    
    # Prioritize sleep for significant sleep deprivation or low alertness
    if time_since_slept > 4 or alertness < 0.5:
        return 3
    
    # Boost alertness if it's moderate and health indicators are stable 
    if 0.5 <= alertness < 0.6 and hypertension < 0.015 and intoxication < 0.03:
        return 1

    # Use beer if suitable periodic interval and stable health
    if time_elapsed >= 300 and time_elapsed % 150 == 0 and hypertension < 0.01 and intoxication < 0.02:
        return 2
    
    # Regular work if all else is stable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
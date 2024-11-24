import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep if any health indicators are critical or have not slept for a long time
    if alertness < 0.4 or hypertension >= 0.75 or intoxication > 0.4 or time_since_slept >= 6:
        return 3  # Prioritize sleep to ensure health
    
    # Coffee only if alertness is low and health indicators are under control
    if alertness < 0.6 and hypertension < 0.7 and intoxication < 0.3:
        return 1  # Boost alertness with coffee
    
    # Work if conditions are optimal
    if alertness >= 0.65 and hypertension < 0.7 and intoxication <= 0.2:
        return 0  # Safe to work
    
    # Default to sleep if no safe work or coffee option
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
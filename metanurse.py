import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if critical health or alertness issues are present
    if alertness < 0.5 or hypertension > 0.07 or intoxication > 0.04 or time_since_slept >= 4.0:
        return 3  # Sleep if any health indicators are concerning.
    
    # Drink beer if stress is suggested by a combination of low alertness and moderate intoxication
    if alertness < 0.6 and intoxication <= 0.06 and hypertension > 0.05:
        return 2  # Relax with a beer to balance stress.
    
    # Use coffee strategically to boost alertness and productivity
    if 0.5 <= alertness < 0.75 and hypertension < 0.04:
        return 1  # Drink coffee for a productivity boost.
    
    # Default to work if conditions allow without significant health risk
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
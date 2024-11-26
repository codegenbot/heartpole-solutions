import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if health metrics are critical or sleep-deprivation is high.
    if hypertension > 0.015 or intoxication > 0.05 or alertness < 0.5 or time_since_slept > 5:
        return 3
    
    # Drink coffee to improve alertness when it's moderately low but safe to do so.
    if 0.5 <= alertness < 0.6 and hypertension < 0.01 and intoxication < 0.03:
        return 1
    
    # Use beer infrequently for productivity boost, within safe health limits.
    if time_elapsed % 400 == 0 and hypertension < 0.008 and intoxication < 0.02:
        return 2
    
    # Default action is to work, ensuring moderate alertness and low health risk.
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
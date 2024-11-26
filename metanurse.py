import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if any health metric is critical or if sleep-deprived
    if hypertension > 0.015 or intoxication > 0.05 or alertness < 0.5 or time_since_slept > 5:
        return 3
    
    # Drink coffee when alertness is lower but safe; prioritize boosting productivity
    if 0.5 <= alertness < 0.6 and hypertension < 0.01 and intoxication < 0.03:
        return 1
    
    # Use beer for productivity boost with stricter safe limits, and occasionally
    if time_elapsed % 400 == 0 and hypertension < 0.008 and intoxication < 0.02:
        return 2
    
    # Default action is work, with stable alertness and low health risk
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
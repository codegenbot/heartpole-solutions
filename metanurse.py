import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Lower health thresholds for safety
    if hypertension > 0.015 or intoxication > 0.04:
        return 3

    # Sleep if significantly deprived of rest or low alertness
    if time_since_slept > 5 or alertness < 0.4:
        return 3
    
    # Use coffee if moderate alertness and health are stable
    if 0.4 <= alertness < 0.7 and hypertension < 0.01 and intoxication < 0.02:
        return 1
    
    # Use beer strategically if long uptime and health stable
    if time_elapsed >= 300 and time_elapsed % 150 == 0 and hypertension < 0.008 and intoxication < 0.015:
        return 2
    
    # Regular work if conditions are optimal
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
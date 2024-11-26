import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if health parameters cross critical thresholds
    if hypertension > 0.012 or intoxication > 0.03:
        return 3

    # Encourage sleep if significantly deprived of rest or low alertness
    if time_since_slept > 4 or alertness < 0.5:
        return 3

    # Drink coffee to enhance alertness if falling slightly low, but ensure not too stressed
    if 0.5 <= alertness < 0.8 and hypertension < 0.01 and intoxication < 0.02:
        return 1

    # Occasionally drink beer and work if uptime is long and health conditions allow
    if time_elapsed >= 250 and time_elapsed % 200 == 0 and hypertension < 0.007 and intoxication < 0.01:
        return 2

    # Default action to work if all parameters are in acceptable ranges
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if hypertension or intoxication too high
    if hypertension > 0.25 or intoxication > 0.12:
        return 3
    # Sleep if alertness is critically low or long time since last sleep
    if alertness < 0.6 or time_since_slept > 6:
        return 3
    # Drink coffee to boost alertness if it's moderately low
    if alertness < 0.8 and hypertension < 0.2 and intoxication < 0.1:
        return 1
    # Use beer as a relaxation and alertness balance, but with caution
    if 0.1 < intoxication < 0.15 and hypertension < 0.18:
        return 2
    # Default to work if no critical issues detected
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
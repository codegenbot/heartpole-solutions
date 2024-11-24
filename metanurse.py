import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep if sleep-deprived or health indicators suggest risk - stricter condition
    if time_since_slept > 6 or hypertension > 0.3 or intoxication > 0.2 or alertness < 0.5:
        return 3
    # Use coffee if alertness is low but not critical and hypertension is low
    if alertness < 0.7 and hypertension < 0.1 and intoxication < 0.15:
        return 1
    # Safe to work if high alertness, low hypertension, and low intoxication
    if alertness > 0.75 and hypertension < 0.1 and intoxication < 0.1:
        return 0
    # Default to just working or moderate stimulant usage if conditions are balanced
    return 2

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
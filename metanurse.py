import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleeping if hypertension or time since last slept is critically high.
    if hypertension > 0.15 or time_since_slept >= 6.5:
        return 3
    # Avoid intoxication overworking, use beer when slightly intoxicated.
    if intoxication > 0.2:
        return 3  # Sleep when intoxicated
    # Drink coffee only under low alertness and low hypertension
    if alertness < 0.5 and hypertension < 0.05:
        return 1
    # Just work if alertness is good and other risks are low
    if alertness >= 0.75 and hypertension < 0.05 and intoxication < 0.1:
        return 0
    # Drink beer if a minor boost is needed and intoxication is manageable
    if intoxication < 0.05:
        return 2
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
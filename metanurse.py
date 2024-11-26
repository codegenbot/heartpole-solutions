import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Better health thresholds
    if intoxication > 0.1 or hypertension > 0.01:
        return 3  # sleep to counteract any health risk
    if time_since_slept >= 7:
        return 3  # more consistent rest to balance productivity
    if alertness < 0.3:
        return 3  # prioritize sleep for low alertness more strictly
    if alertness < 0.5 and hypertension < 0.008 and intoxication < 0.03:
        return 1  # moderate coffee intake if conditions are healthier
    return 0  # default to work if all conditions are acceptable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
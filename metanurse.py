import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if intoxication > 0.03 or hypertension > 0.02 or time_since_slept >= 8:
        return 3  # prioritize sleep for health recovery
    if alertness < 0.5 or time_since_slept >= 5:
        return 3  # ensure sufficient rest time for better productivity
    if alertness < 0.65 and hypertension < 0.015 and intoxication < 0.015:
        return 1  # coffee to boost alertness if conditions aren't optimal
    if alertness >= 0.75 and hypertension <= 0.005 and intoxication <= 0.005:
        return 2  # beer when truly optimal, consider its longer-term benefit carefully
    return 0  # continue working under safe and productive conditions

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
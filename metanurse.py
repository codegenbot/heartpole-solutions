import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # High priority for health: severe sleep deprivation or high risk indicators
    if time_since_slept > 6 or hypertension >= 0.3 or intoxication >= 0.3:
        return 3
    # Work if alert, and health indicators are low
    if alertness >= 0.85 and hypertension < 0.15 and intoxication < 0.15:
        return 0
    # Use coffee to boost alertness if it's declining but health is fine
    if alertness < 0.7 and hypertension < 0.25:
        return 1
    # If neither alertness nor health is optimal, work with caution
    return 2

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
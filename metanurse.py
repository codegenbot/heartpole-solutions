import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize critical health intervention
    if hypertension > 0.6 or intoxication > 0.5 or alertness < 0.2 or time_since_slept > 16:
        return 3
    # Moderate warning intervention
    if time_since_slept > 12 or (hypertension > 0.4 and alertness < 0.3):
        return 3
    # Productive alertness adjustment
    if alertness < 0.3 and hypertension <= 0.4:
        return 1
    if alertness < 0.5 and intoxication <= 0.2:
        return 2
    # Safe and productive work condition
    if alertness >= 0.8 and hypertension <= 0.2 and intoxication <= 0.1:
        return 0
    # Fallback to working when none of the above are triggered
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
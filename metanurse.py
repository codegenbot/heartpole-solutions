import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep conditions based on health risks and alertness
    if alertness < 0.4 or hypertension > 0.6 or intoxication > 0.5 or time_since_slept > 8:
        return 3  # Prioritize sleep for recovery

    # Coffee strategy for low alertness without high hypertension
    if 0.4 <= alertness < 0.5 and hypertension < 0.3:
        return 1  # Coffee intake when conditions allow

    # Beer for hypertension control when safe to do
    if 0.5 < hypertension <= 0.7 and intoxication < 0.2:
        return 2  # Manage hypertension with beer when safe

    # Optimal work condition
    if alertness >= 0.5 and hypertension < 0.3 and intoxication < 0.2:
        return 0  # Continue working under ideal conditions

    return 0  # Default action is to work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
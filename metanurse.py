import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep on critical intoxication or high hypertension
    if intoxication >= 0.006 or hypertension > 0.014:
        return 3

    # Prioritize sleep when alertness drops significantly or extended wakefulness
    if alertness < 0.85 or time_since_slept > 4:
        return 3

    # Coffee to boost productivity if conditions are mildly suboptimal
    if 0.85 <= alertness < 0.95 and hypertension < 0.010:
        return 1

    # Just work if conditions are optimal and time allows
    if alertness >= 0.95 and intoxication <= 0.005 and hypertension <= 0.010:
        return 0

    # Default action is just work
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
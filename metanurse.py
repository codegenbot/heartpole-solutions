import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Adjust sleep threshold to balance rest and work
    if hypertension > 0.15 or intoxication > 0.15 or time_since_slept > 5:
        return 3
    # Utilize coffee to manage alertness without compromising health
    if alertness < 0.6 and hypertension < 0.08 and intoxication < 0.03:
        return 1
    # Maintain work focus when conditions are optimal
    if alertness >= 0.8 and hypertension < 0.05 and intoxication < 0.03:
        return 0
    # Apply beer when a high level of work is completed and it's safe health-wise
    if work_done > 9 and alertness > 0.6 and intoxication < 0.07:
        return 2
    # Default to sleep when uncertain to ensure sustained health
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
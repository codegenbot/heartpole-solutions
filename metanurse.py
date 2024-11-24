import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Aggressively prioritize health (sleep) to prevent negative long-term effects
    if alertness < 0.6 or hypertension > 0.5 or intoxication > 0.3 or time_since_slept > 8 or time_elapsed > 20:
        return 3

    # Encourage coffee usage moderately when alertness is not optimal and health allows
    if 0.6 <= alertness < 0.75 and hypertension <= 0.35 and intoxication <= 0.1:
        return 1

    # Encourage beer before sleep only if it helps improve the sleep decision
    if intoxication < 0.1 and 7 <= time_since_slept <= 8:
        return 2

    # Default to working if conditions are optimal
    if alertness >= 0.75 and hypertension <= 0.25 and intoxication <= 0.05:
        return 0

    # When workload is high, consider sleep for recovery
    if work_done >= 0.8:
        return 3

    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
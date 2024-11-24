def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep more aggressively
    if time_since_slept > 5 or hypertension > 0.7 or intoxication > 0.5:
        return 3
    # Consider sleep based on alertness and sleep deprivation
    if alertness < 0.5 or time_since_slept > 3:
        return 3
    # Allow coffee with a narrower band for moderate alertness and low hypertension
    if 0.5 <= alertness < 0.7 and hypertension < 0.4:
        return 1
    # Default to work if all metrics suggest good conditions
    if alertness > 0.7 and hypertension < 0.3 and intoxication < 0.3:
        return 0
    # Use beer when intoxication suggests a moderate need to relax
    return 2 if 0.3 <= intoxication < 0.5 else 0

import sys

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
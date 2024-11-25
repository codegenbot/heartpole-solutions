def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep to prevent severe health issues
    if hypertension >= 0.12 or intoxication >= 0.05 or alertness < 0.5 or time_since_slept > 5:
        return 3
    # Use coffee under safe conditions to boost alertness and productivity
    if alertness < 0.75 and hypertension < 0.08 and intoxication < 0.03:
        return 1
    # Work in stable health conditions without coffee or sleep
    if alertness >= 0.75 and hypertension < 0.1 and intoxication < 0.03:
        return 0
    # Default sleep to avoid indecision and manage health
    return 3

import sys

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
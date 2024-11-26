import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep when alertness or lack of sleep is critical, or intoxication is high
    if alertness < 0.6 or time_since_slept >= 5 or intoxication > 0.1:
        return 3
    # Use coffee boost only if alertness is moderate and hypertension is low
    if alertness < 0.75 and hypertension < 0.03:
        return 1
    # Allow beer for relaxation if it doesn't significantly increase intoxication
    if 0.75 <= alertness < 0.85 and intoxication < 0.03 and hypertension < 0.02:
        return 2
    # Default to working if alertness and health conditions are stable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
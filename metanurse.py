import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Health priorities
    if hypertension > 0.02 or intoxication > 0.08:
        return 3  # Immediate need for rest
    if time_since_slept >= 5.5:
        return 3  # Need for sleep after a long time

    # Alertness checks
    if alertness < 0.35:
        return 3  # Low alertness, prioritize rest

    # Improve alertness with coffee, conditionally
    if alertness < 0.6 and hypertension < 0.01:
        return 1  # Use coffee wisely, allow slight risk for productivity boost

    # Routine work, if all conditions are favorable
    if 0.6 <= alertness < 0.9 and hypertension < 0.015:
        return 0  # Focus on work

    # Default to working if conditions do not warrant immediate rest
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
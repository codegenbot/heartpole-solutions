import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Health priorities
    if hypertension > 0.025 or intoxication > 0.1:
        return 3  # Immediate need for rest
    if time_since_slept >= 6:
        return 3  # Need for sleep after a long time

    # Alertness checks
    if alertness < 0.4:
        return 3  # Low alertness, prioritize rest

    # Improve alertness with coffee, conditionally
    if alertness < 0.65 and hypertension < 0.012:
        return 1  # Use coffee wisely

    # Routine work, if all conditions are favorable
    if 0.65 <= alertness < 0.9:
        return 0  # Focus on work

    # Default to work to avoid metabolic issues with coffee and beer
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
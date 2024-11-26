import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if showing signs of fatigue or nearing risky conditions:
    if time_since_slept >= 6 or alertness < 0.5:
        return 3
    if hypertension >= 0.05 or intoxication >= 0.1:
        return 3

    # Use coffee cautiously when alertness is low but without overuse:
    if alertness < 0.7:
        if hypertension < 0.045 and intoxication < 0.06:
            return 1
        return 3

    # Allow beer rarely and only when perfect conditions are met:
    if 0.75 <= alertness < 0.85 and hypertension < 0.025 and intoxication < 0.025:
        return 2

    # Default to work when health and alertness metrics are sound:
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
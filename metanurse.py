import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if serious health risks
    if hypertension > 0.015 or intoxication > 0.015 or alertness < 0.3:
        return 3

    # Proactive sleep before alertness and health degrade too much
    if time_since_slept > 2.5 or alertness < 0.35:
        return 3

    # Drink coffee if alertness is slightly declining and health parameters are safe
    if 0.3 <= alertness < 0.5 and hypertension < 0.01 and intoxication < 0.01:
        return 1

    # Work if alertness is sufficient
    if alertness >= 0.5:
        return 0

    # Default to just work if no strong health indications or need for boosts
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
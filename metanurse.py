import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if serious health risks
    if hypertension > 0.02 or intoxication > 0.02 or alertness < 0.25:
        return 3

    # Proactive sleep before alertness and health degrade too much
    if time_since_slept > 3 or alertness < 0.3:
        return 3

    # Drink coffee responsibly if alertness is moderate
    if 0.35 <= alertness < 0.5 and hypertension < 0.015:
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
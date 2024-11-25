import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if serious health risks
    if hypertension > 0.03 or intoxication > 0.025 or alertness < 0.2:
        return 3

    # Sleep proactively before alertness becomes too low
    if time_since_slept > 3.5 or (alertness < 0.35 and time_since_slept > 2.5):
        return 3

    # Drink coffee to boost alertness if hypertension is not too high
    if 0.3 <= alertness < 0.45 and hypertension < 0.02:
        return 1

    # Work if alertness is high enough and health is stable
    if alertness >= 0.45:
        return 0

    # Drink beer if other risks are stable but need to relax slightly
    if alertness < 0.3 and hypertension < 0.02 and intoxication < 0.02:
        return 2

    # Default to just work if no strong health indications or need for boosts
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
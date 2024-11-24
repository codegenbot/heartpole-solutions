import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep when conditions are close to risk levels
    if (
        alertness < 0.4
        or hypertension > 0.7
        or intoxication > 0.4
        or time_since_slept > 6.5
    ):
        return 3

    # Drink coffee to boost alertness if not too risky
    if (
        alertness < 0.55
        and hypertension < 0.55
        and intoxication < 0.2
        and time_since_slept <= 7
    ):
        return 1

    # Work if health metrics indicate good condition
    if alertness >= 0.65 and hypertension < 0.5 and intoxication < 0.15:
        return 0

    # Drink beer cautiously if slightly intoxicated to relax, with mid alertness
    if hypertension < 0.6 and 0.15 <= intoxication < 0.3 and alertness < 0.6:
        return 2

    # Prioritize sleep when past workout cycles show accumulated fatigue with alertness under threshold
    if time_elapsed > 200 and alertness < 0.5:
        return 3

    # Default to sleep if other actions seem unsuitable
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
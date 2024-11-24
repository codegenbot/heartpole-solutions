import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # High priority sleep if critical metrics breached
    if alertness < 0.6 or intoxication > 0.25 or hypertension > 0.7 or time_since_slept >= 4:
        return 3  # Must sleep

    # Work when all metrics are optimal
    if alertness >= 0.85 and hypertension < 0.35 and intoxication < 0.1:
        return 0  # Just work

    # Use coffee when alertness is low but within safe health bounds
    if alertness < 0.75 and 0.3 <= hypertension < 0.6:
        return 1  # Drink coffee and work

    return 0  # Default to just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Enforce sleep if health risk parameters are concerning
    if hypertension > 0.2 or intoxication > 0.1 or time_since_slept > 6:
        return 3  # Sleep

    # Sleep if alertness is critically low
    if alertness < 0.5:
        return 3  # Sleep

    # Consider coffee if alertness is low but health is safe
    if 0.5 <= alertness < 0.8 and hypertension < 0.15 and intoxication < 0.05:
        return 1  # Drink coffee and work

    # Introduce a mechanism to rest periodically for recharge
    if time_elapsed > 150:
        return 3  # Sleep every 150 steps to avoid build-up of fatigue

    # Default to working if everything is safe and alertness is sufficient
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
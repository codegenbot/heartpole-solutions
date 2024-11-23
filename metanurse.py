import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Enforce sleep if any health risk parameters reach critical levels
    if hypertension > 0.40 or intoxication > 0.25 or time_since_slept > 10:
        return 3  # Sleep

    # Sleep if alertness is too low to work effectively
    if alertness < 0.5:
        return 3  # Sleep

    # Consider drinking coffee in more scenarios if it can boost productivity safely
    if 0.5 <= alertness < 0.8 and hypertension <= 0.25 and intoxication <= 0.15:
        return 1  # Drink coffee and work

    # Drink beer to handle high alertness with moderate alcohol impact
    if 0.85 < alertness and intoxication < 0.10 and time_since_slept < 6:
        return 2  # Drink beer and work

    # Default to working if vital signs are within a manageable range
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
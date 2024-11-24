import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleeping if critical thresholds are met or exceed safe limits
    if alertness < 0.3 or hypertension > 0.7 or intoxication > 0.5 or time_since_slept > 8:
        return 3  # Must sleep to recover

    # Favor working when alertness is high and health indicators are in a safe zone
    if alertness > 0.85 and hypertension < 0.5 and intoxication < 0.3:
        return 0  # Just work

    # Use coffee to boost productivity when alertness is moderate and within health limits
    if 0.5 <= alertness <= 0.85 and hypertension < 0.6 and intoxication < 0.4:
        return 1  # Drink coffee and work

    # Consider using beer only when very slightly intoxicated and need a lesser alertness boost
    if 0.4 <= alertness < 0.5 and intoxication < 0.2:
        return 2  # Drink beer and work

    return 3  # Default to sleep to ensure safe recovery

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
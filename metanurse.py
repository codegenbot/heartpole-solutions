import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Tighter control on health indicators
    if hypertension > 0.04 or intoxication > 0.08:
        return 3
    if time_since_slept > 7.0:
        return 3

    # Resource allocation to improve productivity
    if alertness < 0.65 and hypertension < 0.03 and intoxication < 0.03:
        return 1

    # Avoid beer unless alertness is critically low and other indicators are safe
    if alertness < 0.55 and intoxication < 0.04 and hypertension < 0.02:
        return 2

    # Work more when feasible
    if alertness >= 0.8 and hypertension < 0.02 and intoxication < 0.02:
        return 0

    return 3  # Default to rest for safe recovery

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
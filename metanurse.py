import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep on critically low alertness or high hypertension/intoxication
    if alertness < 0.3 or hypertension >= 0.25 or intoxication >= 0.25:
        return 3  # Sleep

    # Sleep if significant time has passed without rest
    if time_since_slept > 10:
        return 3  # Sleep

    # Use coffee only if alertness is moderate and hypertension is very low
    if alertness < 0.6 and hypertension < 0.1:
        return 1  # Drink coffee and work

    # Prefer working when alertness is sufficient
    if alertness >= 0.65:
        return 0  # Just work

    return 0  # Default to work if conditions are moderate

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
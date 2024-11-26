import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension >= 0.03 or intoxication >= 0.03:
        return 3  # Sleep if significant health risks are present

    if time_since_slept > 3.0:
        return 3  # Sleep if the user hasn't slept recently enough

    if alertness < 0.7 and hypertension < 0.02:
        return 1  # Drink coffee if alertness is declining and hypertension is low

    if alertness >= 0.8 and intoxication < 0.01:
        return 0  # Just work if alertness is high and intoxication is negligible

    return 0  # Default to working if none of the conditions trigger more urgent actions

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
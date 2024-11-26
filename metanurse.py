import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension >= 0.02 or intoxication >= 0.02:
        return 3  # Sleep if significant health risks are present

    if time_since_slept > 2.5:
        return 3  # Sleep if the user hasn't slept recently enough

    if alertness < 0.75:
        if hypertension < 0.015:
            return 1  # Drink coffee and work if slightly tired
        return 3  # Otherwise, prefer sleeping if alertness is very low

    if alertness >= 0.85 and intoxication < 0.01:
        return 0  # Work if alertness is high and intoxication is negligible

    return 0  # Default to working if none of the above conditions met

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
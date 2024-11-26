import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep when necessary
    if time_since_slept >= 6 or alertness <= 0.4:
        return 3  # Sleep

    if hypertension >= 0.08 or intoxication > 0.07:
        return 3  # Sleep to mitigate health risks

    if alertness < 0.6 and hypertension < 0.05:
        return 1  # Drink coffee to improve alertness safely

    if alertness > 0.8 and intoxication < 0.02 and hypertension < 0.01:
        return 2  # Drink beer in very optimal conditions

    return 0  # Default to work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
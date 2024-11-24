import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize Sleep for Recovery
    if time_since_slept > 7 or alertness < 0.4 or hypertension > 0.6 or intoxication > 0.5:
        return 3  # Sleep

    # Optimize Coffee Usage
    if 0.4 <= alertness < 0.6 and hypertension <= 0.5 and intoxication < 0.3:
        return 1  # Drink coffee and work

    # Avoid Beer with High Intoxication
    if intoxication < 0.4 and hypertension < 0.4 and alertness < 0.6:
        return 2  # Drink beer and work

    # Encourage Safe Work
    if alertness >= 0.6 and hypertension < 0.4 and intoxication < 0.3:
        return 0  # Just work

    return 0  # Safe default action is to work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if alertness < 0.6 or intoxication > 0.1 or time_since_slept >= 5:
        return 3  # Sleep
    if alertness < 0.75 and hypertension < 0.3 and intoxication <= 0.05:
        return 1  # Drink coffee and work
    if alertness >= 0.9 and hypertension < 0.25:
        return 0  # Work
    return 0  # Work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
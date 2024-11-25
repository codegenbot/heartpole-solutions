import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if (
        time_since_slept > 6
        or alertness < 0.5
        or hypertension >= 0.7
        or intoxication >= 0.2
    ):
        return 3  # More stringent conditions for choosing sleep
    if 0.7 <= alertness <= 0.9 and hypertension < 0.3 and intoxication < 0.15:
        return 1  # Drink coffee and work if alertness is decent but not peak
    if alertness > 0.85 and hypertension < 0.3 and intoxication < 0.1:
        return 0  # Just work if alertness is optimal
    return 0  # Continue working by default

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
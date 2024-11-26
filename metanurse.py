import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if time_since_slept >= 8 or alertness < 0.5 or intoxication > 0.15:
        return 3
    if alertness < 0.7 and hypertension < 0.03 and intoxication < 0.1:
        return 1
    if alertness < 0.65 and intoxication < 0.07:
        return 2
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
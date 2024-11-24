import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.7 or intoxication > 0.6 or time_since_slept > 7 or alertness < 0.5:
        return 3
    if 0.5 <= alertness < 0.65 and hypertension < 0.4 and intoxication < 0.3:
        return 1
    if alertness >= 0.65 and hypertension < 0.35 and intoxication < 0.25:
        return 0
    return 2

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
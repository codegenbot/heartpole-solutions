import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    target_work_done = 0.9
    if hypertension > 0.02 or intoxication > 0.08:
        return 3
    if time_since_slept >= 4 or alertness < 0.3 or work_done >= target_work_done:
        return 3
    if alertness < 0.5 and hypertension < 0.01 and intoxication < 0.05 and time_since_slept < 4:
        return 1
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
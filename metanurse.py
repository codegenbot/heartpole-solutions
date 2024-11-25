import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if alertness < 0.5 or time_since_slept > 6:
        return 3  # prioritize sleep to handle alertness and sleep deprivation

    if 0.5 <= alertness < 0.7 and hypertension < 0.07:
        return 1  # allow coffee use with slightly higher hypertension

    if alertness >= 0.7 and hypertension < 0.07 and intoxication < 0.05:
        return 0  # optimal state for working

    return 0  # default to work if other conditions do not apply

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if (
        alertness < 0.3
        or hypertension > 0.07
        or intoxication > 0.06
        or time_since_slept >= 5.0
    ):
        return 3

    if 0.3 <= alertness < 0.6 and hypertension < 0.06 and intoxication < 0.05:
        return 1

    if alertness >= 0.6 and hypertension < 0.04 and intoxication < 0.03:
        return 0

    if work_done < 0.01 and intoxication <= 0.02 and alertness < 0.2:
        return 2
        
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if (
        alertness < 0.3
        or hypertension > 0.07
        or intoxication > 0.06
        or time_since_slept >= 4.0
    ):
        return 3

    if 0.3 <= alertness < 0.5 and hypertension < 0.05 and intoxication < 0.04:
        return 1

    if alertness >= 0.7 and hypertension < 0.03 and intoxication <= 0.02:
        return 0

    if work_done < 0.01 and intoxication < 0.02 and alertness < 0.2:
        return 2
        
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
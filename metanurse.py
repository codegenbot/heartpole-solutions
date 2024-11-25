import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if (
        alertness < 0.5
        or hypertension > 0.07
        or intoxication > 0.04
        or time_since_slept >= 3.0
    ):
        return 3  # Sleep whenever alertness is low or health indicators are high

    if 0.5 <= alertness < 0.75 and hypertension < 0.05 and intoxication < 0.03:
        return 1  # Drink coffee to boost alertness mildly within safe parameters

    if alertness >= 0.75 and hypertension < 0.03 and intoxication < 0.02:
        return 0  # Optimal conditions for working

    if work_done < 0.01 and intoxication <= 0.01 and alertness < 0.3:
        return 2  # Beer can help stimulate extremely low productivity over time

    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
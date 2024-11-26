import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Strong indicators to reduce health risks:
    if hypertension > 0.04 or intoxication > 0.08:
        return 3
    if time_since_slept > 5:
        return 3

    # Boost alertness with coffee if needed and safe:
    if alertness < 0.6:
        if hypertension < 0.03 and intoxication < 0.03:
            return 1

    # Favor working when alertness is good and health conditions are optimal:
    if alertness > 0.75 and hypertension < 0.02 and intoxication < 0.02:
        return 0

    # Resort to sleeping if safe working or coffee is unsuitable:
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
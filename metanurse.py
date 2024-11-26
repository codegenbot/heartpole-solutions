import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleeping for high health risk or low alertness
    if hypertension > 0.015 or intoxication > 0.08:
        return 3
    if alertness < 0.5 or time_since_slept >= 6:
        return 3
    # Drink coffee if alertness is moderately low and health conditions allow
    if alertness < 0.75 and hypertension < 0.010 and intoxication < 0.04:
        return 1
    # Choose work if alertness is adequate and health is stable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
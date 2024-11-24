import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep if very necessary or health risks are high
    if alertness < 0.4 or hypertension > 0.7 or intoxication > 0.4 or time_since_slept > 7:
        return 3

    # Drink coffee if alertness is low but health is reasonably safe
    if alertness < 0.6 and hypertension < 0.6 and intoxication < 0.25 and time_since_slept <= 7:
        return 1

    # Work in safe and productive conditions
    if alertness >= 0.7 and hypertension < 0.5 and intoxication < 0.2:
        return 0

    # Drink beer only for mild stress relief (usually inappropriate)
    if hypertension < 0.5 and intoxication < 0.3:
        return 2

    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
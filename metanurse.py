import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.12 or intoxication > 0.07 or time_since_slept > 3.5:
        return 3  # Sleep when health metrics indicate risk

    if alertness < 0.8:
        return 3  # Ensure high alertness with sleep

    if 0.8 <= alertness < 0.9 and hypertension < 0.09 and intoxication < 0.04:
        return 1  # Drink coffee and work to boost alertness

    if hypertension < 0.05 and intoxication < 0.02 and alertness >= 0.9:
        return 0  # Work if alert and healthy indicators are good

    if hypertension < 0.07 and intoxication < 0.03 and alertness >= 0.85:
        return 2  # Occasionally drink beer and work if stable

    return 0  # Default to just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
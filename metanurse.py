import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if severe health markers or prolonged sleeplessness
    if hypertension > 0.25 or intoxication > 0.10 or time_since_slept > 5:
        return 3

    # Sleep if alertness is moderately low
    if alertness < 0.65:
        return 3

    # Coffee to boost alertness, with consideration to health
    if 0.65 <= alertness < 0.75 and hypertension <= 0.15 and intoxication <= 0.05:
        return 1

    # Beer only when alertness is quite low, manage intoxication
    if alertness < 0.70 and intoxication <= 0.05:
        return 2

    # Default to just work if stable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
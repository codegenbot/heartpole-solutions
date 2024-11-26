import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleeping if hypertension or intoxication is high or if not slept recently:
    if hypertension > 0.03 or intoxication > 0.04 or time_since_slept > 4:
        return 3

    # Drink coffee to boost alertness only if health permits and alertness is low:
    if alertness < 0.7 and hypertension < 0.02 and intoxication < 0.02:
        return 1

    # Work if conditions are optimal:
    if alertness > 0.75 and hypertension < 0.02 and intoxication < 0.02:
        return 0

    # Default to sleep to maintain health and alertness:
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
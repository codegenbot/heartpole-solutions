import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension >= 0.02 or intoxication > 0.1:
        return (
            3  # Prioritize health by sleeping if hypertension or intoxication is high
        )
    if alertness < 0.4 or time_since_slept >= 8:
        return (
            3  # Sleep if very low alertness or it's been a long time since last sleep
        )
    if 0.4 <= alertness < 0.7:
        return 1  # Drink coffee to boost moderate alertness
    return 0  # Work if conditions are acceptable


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
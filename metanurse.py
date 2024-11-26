import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep for serious health risks
    if hypertension >= 0.1 or intoxication >= 0.25:
        return 3  # Sleep to recover

    # Sleep criteria to maintain alertness
    if alertness < 0.6 or time_since_slept >= 4:
        return 3  # Sleep

    # Drink coffee only if health metrics allow
    if 0.6 > alertness >= 0.5 and hypertension < 0.1 and intoxication < 0.25:
        return 1  # Drink coffee and work

    # Work if alertness is sufficient
    if alertness >= 0.7:
        return 0  # Just work

    # Fallback to default working
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
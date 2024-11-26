import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep for any notable hypertension or intoxication
    if hypertension > 0.01 or intoxication > 0.05:
        return 3  # sleep to address early signs of health risks

    # Sleep for significant sleep deprivation or low alertness
    if time_since_slept >= 4 or alertness < 0.4:
        return 3  # sleep to restore necessary rest and alertness

    # Consider coffee carefully: if moderately tired, but health metrics are low
    if alertness < 0.6 and hypertension < 0.01 and intoxication < 0.03:
        return 1  # boost alertness safely

    # Default to working under ideal conditions
    return 0  # just work when healthy and alert


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
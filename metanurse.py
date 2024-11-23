import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep for health restoration
    if (
        hypertension > 0.7 or intoxication > 0.5 or alertness < 0.25 or 
        time_since_slept >= 12
    ):
        return 3  # Sleep if there's a serious health risk

    # Use coffee to boost alertness under controlled conditions
    if alertness < 0.5 and hypertension <= 0.3 and intoxication <= 0.3:
        return 1  # Drink coffee to increase alertness

    # Opt for beer if moderate hypertension and low intoxication
    if intoxication <= 0.3 and 0.4 < hypertension <= 0.6:
        return 2  # Drink beer for stress relief if it's not too risky

    # Work when conditions are optimal for productivity
    if alertness >= 0.6 and hypertension < 0.4 and intoxication <= 0.2:
        return 0  # Just work if all health metrics are stable

    # Default: if no pressing health concerns, work
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
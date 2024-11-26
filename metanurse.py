import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Adjusted threshold values:
    if hypertension > 0.07 or intoxication > 0.12:
        return 3  # Sleep due to high health risk
    if time_since_slept > 8:
        return 3  # Sleep due to fatigue

    # Adjusted alertness conditions for consuming coffee safely:
    if alertness < 0.65 and hypertension < 0.04 and intoxication < 0.04:
        return 1  # Drink coffee and work

    # Work safely without coffee when conditions are optimal:
    if alertness >= 0.75 and hypertension < 0.03 and intoxication < 0.03:
        return 0  # Just work

    # Resort to sleep when working is not feasible due to low alertness:
    if alertness < 0.55:
        return 3  # Sleep to recover

    # Default action is to work with a drink (beer) if other conditions fail:
    return 2  # Drink beer and work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
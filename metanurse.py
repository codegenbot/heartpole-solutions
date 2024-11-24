import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate response to high risk indicators
    if hypertension > 0.65 or intoxication > 0.55:
        return 3  # Sleep to recover

    # Immediate need for sleep
    if time_since_slept > 7 or alertness < 0.55:
        return 3  # Sleep

    # Optimize productivity with coffee
    if alertness < 0.65 and hypertension < 0.45:
        return 1  # Drink coffee and work

    # Beer as a last resort to low intoxication
    if intoxication < 0.25 and hypertension < 0.25 and alertness < 0.75:
        return 2  # Drink beer and work

    # Optimal condition for working
    if alertness >= 0.75 and hypertension < 0.35 and intoxication < 0.25:
        return 0  # Just work

    # Default to sleep as a fallback
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
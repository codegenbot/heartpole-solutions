import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Lower Hypertension and Intoxication Thresholds
    if hypertension >= 0.12 or intoxication >= 0.3:
        return 3  # Sleep to mitigate health risks

    # Dynamic Alertness Level with work-rest balance
    if time_since_slept >= 5 or alertness < 0.5:
        return 3  # Sleep for necessary recovery

    if alertness < 0.8 and hypertension < 0.12 and intoxication < 0.3:
        return 1  # Drink coffee and continue working

    if alertness >= 0.7:
        return 0  # Just work

    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
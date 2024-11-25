import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 7 or alertness < 0.5 or hypertension > 0.7:
        return 3  # Sleep if conditions indicate tiredness or high risk
    if intoxication >= 0.2:
        return 3  # Sleep if intoxication is significantly high
    if alertness < 0.7:
        return 1  # Prefer coffee to boost alertness if below desirable level
    if alertness >= 0.8 and hypertension < 0.3 and intoxication < 0.1:
        return 0  # Just work if in optimal health conditions
    if intoxication > 0.05:
        return 2  # Drink a beer if slight intoxication might help manage metrics
    return 0  # Default to just work if no preventive measures are required

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
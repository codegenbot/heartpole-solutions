import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate rest if severe health indicators
    if hypertension >= 0.12 or intoxication >= 0.25:
        return 3  # Sleep immediately to mitigate health risks

    # Regular rest based on alertness and time since last sleep
    if time_since_slept >= 4 or alertness < 0.5:
        return 3  # Sleep to recover

    # Consider coffee to boost work only when it's safe and productive
    if alertness < 0.7 and hypertension < 0.1 and intoxication < 0.25:
        if work_done / time_elapsed < 0.4:  # Check productivity rate
            return 1  # Drink coffee to increase alertness and productivity

    # Default to continue working if no interventions are required
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Health checks first
    if hypertension >= 0.02 or intoxication >= 0.1:
        return 3  # sleep if health risk is present
    # Adjust alertness and rest consideration
    if alertness < 0.6 or time_since_slept >= 8:
        return 3  # sleep if alertness is low or hasn't rested sufficiently
    # Adjust productivity with safe health metrics
    if alertness < 0.8 and hypertension < 0.015 and intoxication < 0.05:
        return 1  # drink coffee and work if alertness is mid-range and health is safe
    return 0  # default to work if alertness is high and stable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
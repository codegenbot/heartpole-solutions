import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Adjusting thresholds to better balance productivity and health
    if hypertension > 0.025 or intoxication > 0.15:
        return 3  # sleep if there is any significant health risk
    if alertness < 0.5 or time_since_slept >= 7:
        return 3  # sleep if alertness is low or lack of rest
    if 0.5 <= alertness < 0.75 and hypertension < 0.02 and intoxication < 0.1:
        return 1  # drink coffee and work if marginal alertness and safe health
    if 0.75 <= alertness < 0.9:
        return 0  # just work if alertness is good and health is stable
    return 0  # default to work if conditions are normal

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
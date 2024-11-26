import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.03 or intoxication > 0.2:
        return 3  # sleep if there is significant health risk
    if alertness < 0.5 or time_since_slept >= 8:
        return 3  # sleep if alertness is low or lack of rest
    if 0.6 <= alertness < 0.75 and hypertension < 0.02 and intoxication < 0.05:
        return 1  # drink coffee and work if marginal alertness and safe health
    if alertness >= 0.9 and intoxication < 0.05 and hypertension < 0.03:
        return 0  # just work if alertness is excellent
    if 0.75 <= alertness < 0.9 and intoxication < 0.1:
        return 2  # drink beer and work if alert but slightly stressed
    return 0  # default to work if conditions are normal

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
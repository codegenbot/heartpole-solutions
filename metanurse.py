import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if intoxication > 0.03 or hypertension > 0.015:
        return 3  # sleep for health concerns
    if time_since_slept > 4 or alertness < 0.5:
        return 3  # sleep more often with reduced alertness or longer wake time
    if alertness < 0.6:
        return 1  # use coffee to boost moderate low alertness
    if alertness >= 0.8 and hypertension < 0.007 and intoxication < 0.008:
        return 2  # beer for long productive sessions in optimal health conditions
    return 0  # continue working as default

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
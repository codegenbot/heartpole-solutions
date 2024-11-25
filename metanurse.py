import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.25 or intoxication > 0.3 or time_since_slept >= 10:
        return 3  # sleep if serious health concerns or long period without sleep
    if alertness < 0.4 and hypertension < 0.15 and time_since_slept < 7:
        return 1  # drink coffee to boost alertness safely, but avoid close to required sleep time
    if intoxication < 0.05 and alertness >= 0.7 and hypertension <= 0.1:
        return 0  # if in optimal health conditions, just work
    if hypertension > 0.15 and time_since_slept >= 7:
        return 3  # prefer sleep if moderate hypertension and enough time since last sleep
    return 0  # default to just working

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
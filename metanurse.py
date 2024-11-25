import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.2 or intoxication > 0.2 or time_since_slept >= 8:
        return 3  # sleep if moderate health concerns or quite some time without sleep
    if alertness < 0.5 and hypertension < 0.1 and time_since_slept < 6:
        return 1  # drink coffee to boost alertness if hypertension is low and recently slept
    if alertness >= 0.6 and intoxication < 0.05:
        return 0  # if health is optimal and alertness is adequate, just work
    if hypertension > 0.15:
        return 3  # sleep if moderate hypertension persists
    return 0  # default to just working

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
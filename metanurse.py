import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept >= 4 or alertness < 0.6 or intoxication > 0.2:
        return 3  # prioritize sleep
    if hypertension > 0.05:
        return 3  # sleep to relieve hypertension
    if alertness > 0.8 and hypertension < 0.03 and intoxication < 0.1:
        return 0  # just work
    if alertness >= 0.65 and hypertension < 0.04 and time_elapsed % 3 != 0:
        return 1  # drink coffee and work
    if hypertension >= 0.04 and intoxication < 0.1:
        return 2  # drink beer and work to reduce hypertension cautiously
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept >= 8 or hypertension > 0.3 or intoxication > 0.3:
        return 3  # prioritize sleep under serious health risks
    if alertness < 0.6 and hypertension < 0.25 and intoxication < 0.2:
        return 1  # drink coffee if alertness is low and health parameters permit
    if alertness >= 0.8 and hypertension < 0.2 and intoxication <= 0.05:
        return 0  # just work when conditions are optimal
    if alertness >= 0.7 and intoxication < 0.1:
        return 2  # occasionally use beer if alertness is good and intoxication is low
    return 0  # default to work if conditions are unremarkable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
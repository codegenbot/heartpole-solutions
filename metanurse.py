import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.5 or hypertension > 0.5 or intoxication > 0.3 or time_since_slept > 4:
        return 3  # prioritize sleep under these conditions

    if alertness < 0.7 and hypertension <= 0.3 and intoxication <= 0.1:
        return 1  # drink coffee if alertness is moderate and health allows it

    if alertness >= 0.7 and hypertension <= 0.3 and intoxication <= 0.1:
        return 0  # work if all indicators are healthy

    if 0.1 < intoxication < 0.3 and hypertension < 0.3:
        return 2  # a drink might lower stress or intoxication

    return 3  # default to sleep if unsure

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
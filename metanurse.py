import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 8 or hypertension > 0.75 or alertness < 0.2:
        return 3  # prioritize sleep for better alertness and lower hypertension
    if intoxication > 0.5:
        return 3  # sleep to decrease intoxication
    if alertness < 0.4 and hypertension < 0.6 and intoxication < 0.4:
        return 1  # use coffee to enhance work at moderate health risk
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.2 or hypertension > 0.75 or intoxication > 0.5 or time_since_slept > 8:
        return 3  # Sleep if severely needed
    if 0.2 <= alertness < 0.6 and hypertension <= 0.6 and intoxication <= 0.3:
        return 1  # Coffee if slight alertness boost needed
    if alertness >= 0.6 and hypertension <= 0.5 and intoxication <= 0.2:
        return 0  # Just work
    return 2 if intoxication < 0.3 and hypertension < 0.6 else 3  # Strategic beer or otherwise sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
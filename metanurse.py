import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.3 or hypertension >= 0.2 or intoxication >= 0.15 or time_since_slept >= 8:
        return 3  # Sleep is critical

    if alertness < 0.5:
        return 1  # Coffee to improve alertness if it's moderately low and health stats are not critical

    if hypertension > 0.1 or intoxication > 0.1:
        return 3  # Excess stress indicators suggest sleep

    if time_since_slept >= 6 and alertness < 0.6:
        return 3  # Sleep if alertness is getting low over time

    return 0  # Just work if healthy and alert

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
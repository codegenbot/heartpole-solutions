import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep for lower risk thresholds
    if hypertension > 0.02 or intoxication > 0.08:
        return 3

    # Sleep to recover if nearing exhaustion
    if time_since_slept > 5 or alertness < 0.4:
        return 3

    # Coffee to boost mild alertness decline
    if alertness < 0.55 and hypertension < 0.02:
        return 1

    # Rare beer relaxation, safer if low stress
    if time_elapsed % 300 == 0 and hypertension < 0.015 and intoxication < 0.02:
        return 2

    # Maintain work if conditions are stable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
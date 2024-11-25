import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if critical health risk due to hypertension or intoxication
    if hypertension > 0.03 or intoxication > 0.03:
        return 3

    # Sleep if alertness is low or have not slept for a reasonable time
    if alertness < 0.6 or time_since_slept > 5:
        return 3

    # Drink coffee if moderate alertness and low risk of hypertension
    if 0.6 <= alertness < 0.7 and hypertension < 0.02:
        return 1

    # Work without coffee if alertness high and health is stable
    if alertness >= 0.7 and hypertension < 0.02 and intoxication < 0.02:
        return 0

    # Default to just work cautiously, aim to reduce beer usage
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
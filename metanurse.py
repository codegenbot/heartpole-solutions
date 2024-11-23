import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize health significantly by resting if hypertension or intoxication exceed very safe limits
    if hypertension > 0.2 or intoxication > 0.1:
        return 3

    # Must sleep when alertness is critically low or it's been too long since last sleep
    if alertness < 0.4 or time_since_slept > 12:
        return 3

    # Use coffee to safely boost productivity when fatigue approaches moderate levels
    if alertness < 0.6 and hypertension <= 0.1 and intoxication <= 0.02:
        return 1

    # Default to just working when conditions don't demand immediate changes
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
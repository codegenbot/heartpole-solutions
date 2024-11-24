import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Critical health indicators demand immediate sleep
    if hypertension > 0.7 or intoxication > 0.5 or time_since_slept > 12:
        return 3  # Sleep

    # Prevent moderate health discomfort by resting
    if 8 <= time_since_slept <= 12 and (hypertension > 0.6 or intoxication > 0.4):
        return 3  # Sleep

    # Enhance focus with coffee when significantly drowsy but stable health
    if alertness < 0.4 and hypertension < 0.3 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # Optimal alertness facilitates direct work approach
    if 0.7 <= alertness <= 1.0 and hypertension < 0.5 and intoxication < 0.2:
        return 0  # Just work

    # Minor alertness boost with coffee if health is stable
    if 0.5 <= alertness < 0.7 and hypertension < 0.3 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # For unexpected scenarios, ensure a fallback to rest
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
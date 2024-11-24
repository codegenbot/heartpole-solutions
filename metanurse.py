import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.3 or hypertension > 0.7 or intoxication > 0.4 or time_since_slept > 6:
        return 3  # Sleep if necessary

    if 0.3 <= alertness < 0.5 and hypertension <= 0.5 and intoxication <= 0.3:
        return 1  # Coffee when more productivity is beneficial

    if alertness >= 0.5 and hypertension <= 0.4 and intoxication <= 0.2:
        return 0  # Sustain working under optimal conditions

    return 2 if intoxication <= 0.2 and hypertension <= 0.5 else 3  # Use beer if it's beneficial, else sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
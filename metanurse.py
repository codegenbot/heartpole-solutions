import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness <= 0.6 or hypertension > 0.3 or intoxication > 0.15 or time_since_slept >= 6:
        return 3  # Sleep if alertness is low, hypertension/intoxication is high, or haven't slept for a long time
    if alertness < 0.75 and hypertension <= 0.2 and intoxication <= 0.1:
        return 1  # Drink coffee to boost energy if conditions are manageable
    if alertness > 0.9 and intoxication < 0.05 and hypertension <= 0.2:
        return 2  # Drink beer if in optimal condition and performance is high
    return 0  # Continue working if no specific action is needed

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
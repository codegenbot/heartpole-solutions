import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep for low alertness or high risk thresholds
    if alertness < 0.5 or hypertension > 0.55 or intoxication > 0.25 or time_since_slept > 8:
        return 3  # Sleep

    # Drink coffee if alertness is slightly reduced but manageable
    if alertness < 0.65 and hypertension <= 0.5 and intoxication <= 0.2:
        return 1  # Drink coffee and work

    # Maintain work if in optimal or good condition
    if alertness >= 0.65 and hypertension <= 0.4 and intoxication <= 0.15:
        return 0  # Just work

    # Consider beer if moderate stress levels are present
    if hypertension < 0.5 and intoxication <= 0.3:
        return 2  # Drink beer and work

    return 3  # Default to sleep as a safe action

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
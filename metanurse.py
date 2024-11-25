import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep for critical health issues
    if hypertension > 0.2 or intoxication > 0.1:
        return 3
    # Rest if highly fatigued or if there's been a long time without sleep
    if alertness < 0.7 or time_since_slept > 5:
        return 3
    # Drink coffee to improve alertness safely
    if alertness < 0.85 and hypertension < 0.15 and intoxication < 0.08:
        return 1
    # Default to work if conditions are stable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
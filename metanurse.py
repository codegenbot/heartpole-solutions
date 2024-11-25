import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 8 or alertness < 0.3 or hypertension > 0.2 or intoxication > 0.15:
        return 3  # Sleep to recover health
    if alertness < 0.6 and hypertension < 0.15 and intoxication < 0.05 and time_since_slept <= 5:
        return 1  # Drink coffee to boost productivity
    if time_elapsed > 12 and work_done < 0.3:
        return 1  # Encourage coffee if work is less and overtime is risked
    return 0  # Just work as default action

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.7 or intoxication > 0.4 or time_since_slept > 6:
        return 3  # More frequent need for sleep to maintain health
    if alertness < 0.5:
        return 3  # Increase alertness threshold for sleep
    if alertness < 0.7 and hypertension < 0.6 and intoxication < 0.2:
        return 1  # Prefer coffee over being under-productive
    if alertness >= 0.75 and hypertension < 0.3 and intoxication < 0.1:
        return 0  # Strictly enforce optimal work conditions
    if hypertension < 0.6 and intoxication < 0.3:
        return 2  # Healthier intoxication threshold for beer
    return 3  # Default remains as sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
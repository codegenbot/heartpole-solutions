import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.18 or intoxication > 0.09:
        return 3  # Sleep to recover from high health risks

    if alertness < 0.6 or time_since_slept > 6:
        return 3  # Sleep if alertness is too low or lack of adequate sleep

    if alertness < 0.8 and hypertension < 0.12 and intoxication < 0.05:
        return 1  # Drink coffee to boost alertness if hypertension is stable

    if time_elapsed > 500 and (hypertension < 0.1 and intoxication < 0.03):
        return 2  # Relax with a beer if workload is high and health is stable
    
    return 0  # Default: just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
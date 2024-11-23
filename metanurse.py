import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Adjusted thresholds for better balance between work and health
    if hypertension >= 0.18 or intoxication >= 0.12 or time_since_slept >= 8:
        return 3  # Sleep

    # Use coffee more liberally when alertness is low and health metrics are within safe bounds
    if alertness < 0.65 and hypertension < 0.1 and intoxication < 0.08:
        return 1  # Drink coffee and work

    # Opt for work if high alertness and low health risks are evident
    if alertness >= 0.6 and hypertension < 0.1 and intoxication < 0.1:
        return 0  # Just work

    # Default to sleeping if nothing else supports continued productivity
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
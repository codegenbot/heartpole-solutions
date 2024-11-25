import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if alertness < 0.3 or hypertension > 0.7 or intoxication > 0.5 or time_since_slept > 16:
        return 3  # Sleep to manage health risks effectively
    if alertness >= 0.7 and hypertension < 0.5 and intoxication < 0.2:
        return 0  # Just work for maximum productivity
    if alertness >= 0.4 and hypertension < 0.6 and intoxication < 0.4:
        return 1  # Coffee and work to boost alertness slightly
    return 3  # Default to sleep for maintaining health balance

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
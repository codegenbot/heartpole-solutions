import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep to manage health proactively
    if hypertension >= 0.2 or intoxication > 0.15 or time_since_slept > 4 or alertness < 0.4:
        return 3  # Sleep

    # Use coffee cautiously to boost alertness without escalating hypertension
    if alertness < 0.5 and hypertension < 0.18:
        return 1  # Drink coffee and work

    # Optimal condition for work with safe health levels
    if alertness >= 0.7 and hypertension < 0.12 and intoxication < 0.08:
        return 0  # Just work

    # Avoid beer due to intoxication risk and focus on rest
    return 3  # Default to sleep for better health management

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
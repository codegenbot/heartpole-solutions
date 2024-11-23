import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.3 or intoxication > 0.25 or time_since_slept > 6:
        return 3  # Sleep more readily to prevent health issues
    if alertness < 0.4 and hypertension < 0.2 and intoxication < 0.15:
        return 1  # Moderate coffee use for alertness boosts
    if alertness > 0.65 and hypertension < 0.2 and intoxication <= 0.05:
        return 0  # Prioritize work if metrics are optimal
    if work_done > 20 and alertness > 0.5 and intoxication < 0.1:
        return 2  # Reward with relaxed work after significant progress
    return 3  # Default to sleep for overall health

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.4 or hypertension > 0.3 or intoxication > 0.2 or time_since_slept > 8:
        return 3  # Prioritize sleep under more conditions
    if alertness < 0.7 and hypertension < 0.15 and intoxication < 0.1:
        return 1  # Looser conditions for using coffee to boost alertness
    if alertness > 0.8 and hypertension < 0.2 and intoxication < 0.1:
        return 0  # Work directly if conditions are optimal
    return 0  # Default to working if no other condition is met

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
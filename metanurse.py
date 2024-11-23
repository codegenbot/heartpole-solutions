import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.35 or intoxication > 0.3 or time_since_slept > 7:
        return 3  # Sleep more restfully if health metrics are poor
    if alertness < 0.5 and hypertension < 0.25 and intoxication < 0.2:
        return 1  # Drink coffee moderately to boost alertness
    if alertness > 0.7 and intoxication <= 0.1:
        return 0  # Work if conditions are optimal
    if work_done > 25 and intoxication < 0.15:
        return 2  # Allow relaxation with beer after substantial work
    return 3  # Default to sleep for overall health

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
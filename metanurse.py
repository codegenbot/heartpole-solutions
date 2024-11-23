import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.35 or intoxication > 0.35 or time_since_slept > 7:
        return 3  # Sleep if health metrics exceed safer thresholds
    if alertness < 0.6 and hypertension < 0.3 and intoxication < 0.2:
        return 1  # Drink coffee if alertness is low with safe hypertension and intoxication levels
    if alertness >= 0.7 and hypertension < 0.3 and intoxication < 0.1:
        return 0  # Work if alertness is optimal and other metrics are very safe
    if work_done > 15 and alertness > 0.5 and intoxication < 0.1 and hypertension < 0.2:
        return 2  # Conditional relaxation with beer
    return 3  # Default to sleep if ambiguous

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
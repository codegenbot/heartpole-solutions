import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.4 or hypertension > 0.12 or intoxication > 0.04 or time_since_slept > 6:
        return 3  # Prioritize sleep more aggressively
    if alertness < 0.6 and hypertension <= 0.1 and intoxication < 0.03:
        return 1  # Use coffee to improve alertness with slightly relaxed conditions
    if hypertension < 0.08 and intoxication < 0.02 and alertness >= 0.5:
        return 0  # Work if alertness is moderate and no health risks are present
    return 0  # Default fallback to continue working

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Aggressively prioritize sleep if any serious condition is met
    if alertness < 0.4 or hypertension > 0.12 or intoxication > 0.04 or time_since_slept > 6:
        return 3
    # Use coffee if alertness is low but within a safer range of hypertension and intoxication
    if alertness < 0.6 and hypertension <= 0.1 and intoxication < 0.03:
        return 1
    # Default to just work if conditions are within a safe range
    if hypertension < 0.08 and intoxication < 0.02 and alertness >= 0.5:
        return 0
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
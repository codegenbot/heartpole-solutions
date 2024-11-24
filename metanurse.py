import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep first if necessary
    if time_since_slept > 6 or alertness < 0.4 or hypertension > 0.8:
        return 3

    # Drink coffee if alertness is moderate and health metrics are within safer limits
    if alertness < 0.7 and hypertension < 0.65 and intoxication < 0.3:
        return 1

    # Work if conditions are optimal
    if alertness >= 0.8 and hypertension < 0.5 and intoxication < 0.2:
        return 0

    # Drink beer if relaxed state is desirable and safe
    if hypertension < 0.35 and intoxication < 0.45:
        return 2

    # Default to sleeping if unsure
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
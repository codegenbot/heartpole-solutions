import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Revised thresholds for better balance
    if intoxication > 0.05 or hypertension > 0.02:
        return 3  # sleep when health risk indicators are high
    if time_since_slept >= 6 and alertness < 0.6:
        return 3  # more frequent sleep if alertness is low and time since last slept is considerable
    if alertness < 0.4:
        return 3  # prioritize sleep for low alertness
    if alertness < 0.7 and hypertension < 0.01 and intoxication < 0.02:
        return 1  # coffee to boost alertness when health indicators allow
    if alertness >= 0.7 and hypertension < 0.008 and intoxication < 0.01:
        return 2  # beer only if all conditions are very good, for longer working sessions
    return 0  # default to work if all conditions are acceptable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
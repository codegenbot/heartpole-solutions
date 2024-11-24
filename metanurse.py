import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if any critical health metric is breached
    if alertness < 0.5 or hypertension > 0.6 or intoxication > 0.3 or time_since_slept > 10:
        return 3

    # Coffee can help improve alertness in controlled health states
    if alertness < 0.6 and hypertension <= 0.4 and intoxication <= 0.15:
        return 1

    # Working is prioritized under stable and optimal alertness
    if alertness >= 0.75 and hypertension <= 0.4 and intoxication <= 0.1:
        return 0

    # Beer can be chosen under low intoxication and hypertension
    if intoxication < 0.05 and hypertension < 0.3:
        return 2

    # Default to sleep if health metrics are ambiguous or mixed
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
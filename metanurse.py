import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Critical health management: Sleep if high risk
    if hypertension > 0.03 or intoxication > 0.04:
        return 3
    if time_since_slept > 5:
        return 3

    # Strategic use of coffee: Only when necessary
    if alertness < 0.6 and hypertension < 0.02 and intoxication < 0.02:
        return 1

    # Work if conditions are optimal
    if alertness >= 0.7 and hypertension < 0.015 and intoxication < 0.015:
        return 0

    # Ensure proper rest if workload is significant
    if work_done > 10 and time_elapsed > 20:
        return 3

    # Default fallback to ensure recovery through sleep
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
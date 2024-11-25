import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Critical: Prioritize sleep if any levels require urgent recovery
    if alertness < 0.3 or hypertension > 0.8 or intoxication > 0.5 or time_since_slept > 12:
        return 3  # Urgent need for sleep

    # Productive yet cautious: utilize coffee
    if 0.5 <= alertness < 0.8 and hypertension < 0.6 and intoxication < 0.1:
        return 1  # Coffee and work

    # Consider beer only under extremely low stress and intoxication
    if alertness < 0.5 and hypertension < 0.4 and intoxication < 0.1:
        return 2  # Beer and relax while working

    # If already alert without issues, continue working
    if alertness > 0.8 and hypertension < 0.5 and intoxication < 0.05:
        return 0  # Just work

    # Default to sleep if no other options are suitable
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
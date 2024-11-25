import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep during low alertness or when health parameters suggest risks
    if alertness < 0.75 or time_since_slept > 5 or hypertension >= 0.04 or intoxication >= 0.05:
        return 3

    # Coffee only when moderate alertness, low hypertension, minimal intoxication
    if 0.75 <= alertness < 0.85 and time_since_slept <= 3 and hypertension < 0.02 and intoxication < 0.02:
        return 1

    # Just work if alertness is sufficiently high to maintain productivity
    if alertness >= 0.85:
        return 0

    # Beer as a fallback if no immediate health issues and alertness is low
    if intoxication < 0.03 and hypertension < 0.03:
        return 2
      
    # Fallback to sleep if none of the conditions are safe
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
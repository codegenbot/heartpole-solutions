import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if alertness < 0.5 or hypertension > 0.06 or intoxication > 0.07:
        return 3  # Sleep if severely impaired or under high hypertension/intoxication

    if alertness < 0.7 or time_since_slept > 4.0:
        return 3  # Sleep if moderately alert or overdue long sleep

    if alertness < 0.8 and hypertension <= 0.03:
        return 1  # Coffee helps maintain focus without high BP

    if alertness >= 0.8 and intoxication <= 0.05:
        return 2  # Beer to balance relaxation

    return 0  # Continue working in all other safe conditions

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
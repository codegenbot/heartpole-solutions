import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # 1. Prioritize sleep if any major health indicators are triggered
    if alertness < 0.5 or hypertension > 0.06 or intoxication > 0.07:
        return 3  # Sleep if severely impaired or under high hypertension/intoxication

    # 2. Moderate cure for lower thresholds
    if alertness < 0.7 or time_since_slept > 4.0:
        return 3  # Sleep if moderately alert or overdue for sleep

    # 3. Use coffee if alertness is starting to wane but hypertension is low
    if alertness < 0.8 and hypertension <= 0.03:
        return 1  # Coffee helps maintain focus without high BP

    # 4. Consider beer for light intoxication and when alertness is good
    if alertness >= 0.8 and intoxication <= 0.05:
        return 2  # Beer to balance relaxation

    # 5. Default to work when all conditions are optimal or minimal alertness loss
    return 0  # Continue working in all other safe conditions


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
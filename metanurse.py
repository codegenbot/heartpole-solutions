import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate health concerns
    if hypertension > 0.15 or intoxication > 0.2:
        return 3  # sleep to alleviate critical health issues

    # Consider sleeping if significantly fatigued or overdue
    if time_since_slept > 8 or alertness < 0.4:
        return 3  # ensure recovery through sleep

    # Utilize coffee when safe and needing a moderate boost
    if 0.4 <= alertness < 0.7 and hypertension < 0.1:
        return 1  # coffee is safe and beneficial here

    # Most productive state without risks
    if alertness >= 0.7 and hypertension < 0.1 and intoxication < 0.1:
        return 0  # keep working productively

    # Beer can relax but only when near idle thresholds
    if work_done < 0.1 and intoxication <= 0.1:
        return 2  # light beer if conditions are safe

    # Default back to working when conditions are not critical
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
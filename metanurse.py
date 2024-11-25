import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if alertness is low or lack of sleep
    if alertness < 0.6 or time_since_slept > 8:
        return 3  # sleep

    # Reduce work if hypertension or intoxication levels are above safe thresholds
    if hypertension >= 0.1 or intoxication >= 0.1:
        return 3  # sleep and recover from poor health

    # Allow a safe amount of coffee for alertness only if health is stable
    if alertness < 0.8 and hypertension < 0.05:
        return 1  # coffee and work

    # Optimal state to just work
    if alertness >= 0.8:
        return 0  # work

    return 0  # default action to work if no specific issue

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
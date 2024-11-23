import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize health - minimizing risks first
    if hypertension >= 0.7 or intoxication >= 0.7:
        return 3  # Sleep if there's a substantial health risk

    if time_since_slept > 10:
        return 3  # Sleep after adequate time to prevent exhaustion

    # Coffee to increase alertness only under moderate hypertension
    if alertness < 0.5 and hypertension <= 0.5:
        return 1  # Drink coffee and work for optimal boost

    # Maintain working pace if conditions are generally good
    if 0.5 <= alertness <= 0.7 and hypertension < 0.5 and intoxication < 0.5:
        return 0  # Just work if parameters are balanced

    # Reduce excessive alertness if low intoxication
    if alertness > 0.8 and intoxication <= 0.3:
        return 2  # Drink beer and work when overly alert

    # Default to regular work to ensure continuous productivity with low health impact
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
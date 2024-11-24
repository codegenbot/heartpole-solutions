import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleeping more when alertness is low
    if alertness < 0.7 or time_since_slept > 8:
        return 3
    if hypertension >= 0.5:  # Be more cautious with hypertension
        return 3
    if intoxication >= 0.3:  # Be more cautious with intoxication
        return 3
    if 0.1 <= intoxication < 0.3 and alertness > 0.75:
        return 2
    if alertness < 0.85 and hypertension <= 0.3 and intoxication < 0.1:
        return 1
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
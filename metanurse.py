import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.02 or intoxication > 0.07:
        return 3  # immediately sleep due to potentially serious health issues
    if time_since_slept >= 5:
        return 3  # sleep to avoid longer-term health impacts and maintain productivity
    if alertness < 0.5 and hypertension < 0.01 and intoxication < 0.02:
        return 1  # safely boost alertness with coffee
    if alertness >= 0.6:
        return 0  # work normally
    return 3  # otherwise, prioritize rest

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
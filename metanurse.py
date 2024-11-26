import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.015 or intoxication > 0.1:
        return 3  # sleep if moderate health risks
    if alertness < 0.4 or time_since_slept >= 8:
        return 3  # sleep to maintain alertness and avoid overwork
    if 0.4 <= alertness < 0.7 and hypertension < 0.01 and intoxication < 0.08:
        return 1  # use coffee if alertness is marginal and health parameters are safe
    return 0  # work if all metrics are stable with slightly conservative thresholds

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
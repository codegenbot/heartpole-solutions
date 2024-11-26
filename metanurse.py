import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Tighter health thresholds
    if intoxication > 0.15 or hypertension > 0.015:
        return 3  # sleep to counteract risks
    if time_since_slept >= 6:
        return 3  # rest is needed sooner
    # Avoid caffeine when health is at risk
    if alertness < 0.4:
        return 3  # prioritize sleep for very low alertness
    if 0.4 <= alertness < 0.5 and hypertension < 0.01 and intoxication < 0.05:
        return 1  # moderate coffee intake if health is good
    return 0  # default to just work if conditions are stable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
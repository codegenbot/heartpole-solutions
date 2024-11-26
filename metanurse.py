import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Lower thresholds for hypertension and intoxication
    if hypertension > 0.01 or intoxication > 0.10:
        return 3  # sleep if health risk is indicated
    if alertness < 0.5:
        return 3  # sleep to recover alertness
    if time_since_slept >= 8 or time_since_slept >= 6 and alertness < 0.7:
        return 3  # ensure regular sleep or when alertness is dropping
    if alertness < 0.7 and hypertension < 0.008 and intoxication < 0.08:
        return 1  # use coffee cautiously to boost alertness
    return 0  # work if conditions are favorable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
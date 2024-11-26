import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Stricter thresholds for proactive health management
    if hypertension > 0.005 or intoxication > 0.05:
        return 3  # sleep if health risk is indicated
    if alertness < 0.6:
        return 3  # sleep to recover alertness
    if time_since_slept >= 7 or (time_since_slept >= 5 and alertness < 0.7):
        return 3  # ensure regular sleep or when alertness is dropping
    if alertness < 0.7 and hypertension < 0.005 and intoxication < 0.05:
        return 1  # use coffee cautiously to boost alertness
    return 0  # work if conditions are favorable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
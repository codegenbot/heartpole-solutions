import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.12 or intoxication > 0.1 or time_since_slept >= 8 or alertness < 0.4:
        return 3  # Prioritize sleep earlier to prevent health issues
    if hypertension < 0.05 and intoxication < 0.02 and alertness > 0.6:
        return 1  # Coffee only when safe and desired alertness level is low
    if alertness < 0.5: 
        return 2  # Beer only when risky health metrics are low; this is less preferable
    return 0  # Work when there are no immediate health risks

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
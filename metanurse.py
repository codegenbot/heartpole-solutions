import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.4 or hypertension > 0.1 or intoxication > 0.1 or time_since_slept >= 6.0:
        return 3  # Rest is a priority if any critical threshold is met
    if 0.4 <= alertness < 0.6 and hypertension < 0.05 and intoxication < 0.03:
        return 1  # Coffee can help transition from moderate to high alertness
    if alertness >= 0.7 and hypertension < 0.03 and intoxication < 0.03:
        return 0  # Optimal conditions for work
    if work_done < 0.2 and alertness < 0.5 and time_since_slept < 3.0:
        return 2  # Beer mainly if overall productivity is very low and health is not at risk
    return 0  # Work by default unless rest or boost is needed

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
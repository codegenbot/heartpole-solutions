import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for high-risk hypertension or intoxication
    if hypertension > 0.03 or intoxication > 0.1:
        return 3
    
    # Mandatory sleep if alertness is critically low or deprived
    if time_since_slept > 6 or alertness < 0.35:
        return 3
    
    # Coffee boost if alertness is low but health is relatively stable
    if alertness < 0.5 and hypertension < 0.025 and intoxication < 0.05:
        return 1

    # Avoid beer unless stress is a cyclic pattern and safe; use time as a modulator
    if time_elapsed % 150 == 0 and hypertension < 0.02 and intoxication < 0.03:
        return 2

    # Default work if health indicators remain stable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
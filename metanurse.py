import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if alertness is critically low or health is at risk
    if alertness < 0.3 or hypertension > 0.6 or time_since_slept > 12:
        return 3  # Sleep

    # Use coffee more proactively across moderate conditions
    if 0.5 <= alertness <= 0.8 and hypertension < 0.5 and intoxication < 0.1 and time_since_slept < 10:
        return 1  # Coffee and work

    # Use beer for quicker replenishment at low alertness but safe overall conditions
    if alertness < 0.5 and hypertension < 0.3 and intoxication < 0.2:
        return 2  # Beer and work

    # Dangerous signs trigger rest without delay
    if hypertension > 0.7 or intoxication > 0.25:
        return 3  # Sleep

    # Work in safe conditions
    if alertness > 0.8 and hypertension < 0.5 and intoxication < 0.1:
        return 0  # Work

    # Use downtime for rest if unsure or at risk
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
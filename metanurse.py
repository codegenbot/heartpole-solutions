import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if critical health metrics are breached or tiredness is high
    if alertness < 0.6 or hypertension > 0.5 or intoxication > 0.25 or time_since_slept > 8:
        return 3

    # Work & drink coffee if moderate alertness and safe health metrics
    if alertness < 0.75 and hypertension <= 0.35 and intoxication <= 0.2:
        return 1

    # Prioritize work if alertness high and safe health metrics
    if alertness >= 0.7 and hypertension <= 0.4 and intoxication <= 0.1:
        return 0

    # Default to sleep in any unclear health conditions
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
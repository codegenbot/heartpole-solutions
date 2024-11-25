import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if alertness is too low or if health indicators signal risk
    if alertness < 0.5 or hypertension > 0.15 or intoxication > 0.1 or time_since_slept > 8:
        return 3

    # Use coffee more liberally within safe hypertension levels
    if alertness < 0.6 and hypertension < 0.09 and intoxication < 0.02 and time_since_slept < 6:
        return 1

    # Work if conditions are favorable
    if alertness >= 0.65 and hypertension <= 0.075 and intoxication <= 0.02:
        return 0

    # Allow beer if work is minimal but within health safety
    if work_done < 0.1 and alertness > 0.6 and hypertension < 0.06 and intoxication < 0.01:
        return 2

    # Default to working with basic conditions
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep when necessary health indicators show fatigue or stress
    if alertness < 0.6 or hypertension > 0.5 or intoxication > 0.4 or time_since_slept > 7.5:
        return 3  # Must sleep

    # Choose coffee for productivity if reasonable health metrics allow
    if alertness < 0.75 and hypertension < 0.5 and intoxication <= 0.3:
        return 1  # Drink coffee and work

    # Direct work when health indicators are optimal
    if alertness >= 0.75 and hypertension <= 0.3 and intoxication < 0.2:
        return 0  # Just work

    # Use beer strategically when alertness needs a slight boost
    if 0.7 <= alertness <= 0.75 and hypertension < 0.4 and intoxication < 0.3:
        return 2  # Drink beer and work

    return 0  # Default to just work if uncertain

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
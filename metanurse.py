import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate need for sleep
    if alertness < 0.5 or hypertension > 0.7 or intoxication > 0.4 or time_since_slept > 7:
        return 3  # Sleep

    # Work with coffee boost when alertness is moderate and no health risks
    if 0.5 <= alertness <= 0.7 and hypertension < 0.5 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # Just work if very alert and healthy
    if alertness > 0.7 and hypertension < 0.3 and intoxication < 0.1:
        return 0  # Just work

    # Avoid using beer for this scenario as it increases intoxication
    return 3  # Default to sleep for safety

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
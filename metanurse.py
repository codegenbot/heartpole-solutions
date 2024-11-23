import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if time_since_slept > 6 or hypertension > 0.2 or intoxication > 0.1:
        return 3  # Sleep is mandatory for extreme conditions

    if alertness < 0.7:
        return 3  # Sleep to mitigate low alertness

    if alertness < 0.9:
        return 1  # Drink coffee when alertness is moderate

    if intoxication < 0.05 and hypertension < 0.05:
        return 0  # Work when healthy and alertness is high

    return 2  # Drink beer as a last resort to slightly lower stress (pleasant action)

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
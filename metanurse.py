import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness <= 0.6 or hypertension >= 0.3 or intoxication >= 0.1 or time_since_slept > 5:
        return 3  # Prioritize sleep more conservatively
    if alertness < 0.75 and hypertension < 0.1 and intoxication < 0.05:
        return 1  # Coffee only if health factors are under control
    if alertness > 0.9 and intoxication < 0.02:
        return 2  # Beer only if very alert and sober
    return 0  # Otherwise, work without boosts

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
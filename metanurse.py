import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Always prioritize sleep if very low alertness or long waking time
    if alertness < 0.4 or time_since_slept > 6 or hypertension > 0.6:
        return 3  # Sleep

    # Prefer to just work if conditions are ideal
    if alertness > 0.8 and hypertension < 0.2 and intoxication == 0.0:
        return 0  # Just work

    # Use coffee if alertness is moderate, controlling hypertension
    if 0.5 <= alertness <= 0.8 and hypertension < 0.4:
        return 1  # Drink coffee and work

    # Use beer only if necessary, prioritizing health concerns last
    if alertness < 0.5 and intoxication < 0.2 and hypertension < 0.3:
        return 2  # Drink beer and work

    # Default action often involves rest when conditions aren't favoring work
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
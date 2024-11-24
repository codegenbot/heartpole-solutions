import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep for serious health issues or when time_since_slept is high
    if time_since_slept > 8 or hypertension >= 0.8 or intoxication >= 0.7 or alertness < 0.4:
        return 3
    # Opt for coffee if alertness is moderate and other conditions are mild
    if alertness < 0.6 and hypertension < 0.5 and intoxication < 0.4:
        return 1
    # Default to work if alertness is high and health metrics are well within safe levels
    if alertness >= 0.7 and hypertension < 0.3 and intoxication < 0.2:
        return 0
    # Use beer to balance in less critical cases for mild intoxication
    return 2 if intoxication < 0.5 else 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
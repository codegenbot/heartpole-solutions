import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.6 or intoxication > 0.4:
        return 3  # Sleep due to health risks
    if time_since_slept > 8:
        return 3  # Sleep due to prolonged wakefulness
    if alertness < 0.5 and hypertension < 0.5:
        return 1  # Drink coffee to boost alertness
    if work_done < 0.8 and alertness >= 0.5:
        return 0  # Work if alertness is sufficient
    return 3  # Default to sleeping if no other condition is met

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
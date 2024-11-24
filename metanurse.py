import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.3 or hypertension > 0.8 or intoxication > 0.5 or time_since_slept > 10:
        return 3  # Prioritize health by sleeping

    if alertness >= 0.7 and hypertension <= 0.5 and intoxication < 0.2:
        return 0  # Work if in optimal condition

    if 0.5 <= alertness < 0.7 and hypertension < 0.6 and intoxication <= 0.3:
        return 1  # Use coffee to boost alertness slightly

    if alertness < 0.5 and intoxication <= 0.3 and hypertension < 0.7:
        return 2  # Use beer to decrease stress (lower hypertension)

    return 3  # Default to sleeping if conditions are risky

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
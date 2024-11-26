import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep to prevent severe health risks
    if hypertension > 0.02 or intoxication > 0.02 or alertness < 0.25:
        return 3

    # Proactive sleep to maintain alertness
    if time_since_slept > 2.5 or (alertness < 0.5 and time_since_slept > 1.5):
        return 3

    # Coffee for alertness boost when health metrics are stable
    if 0.35 <= alertness < 0.5 and hypertension < 0.015:
        return 1

    # Work if still alert and health metrics are stable
    if alertness >= 0.5 and hypertension < 0.02 and intoxication < 0.02:
        return 0

    # Beer only if moderately necessary to relax and health metrics allow
    if alertness < 0.35 and hypertension < 0.015 and intoxication < 0.015:
        return 2

    # Default to just work if no immediate health concerns
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
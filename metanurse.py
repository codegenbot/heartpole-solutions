import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep for extreme critical health conditions or poor alertness
    if alertness < 0.5 or hypertension > 0.3 or intoxication > 0.2 or time_since_slept > 8:
        return 3  # Sleep immediately for critical health

    # Reduce productivity level if health indicators show mild risk
    if hypertension > 0.2 or intoxication > 0.15:
        return 0  # Just work lightly to avoid health issues

    # Use coffee for moderate alertness boost when health is stable
    if alertness < 0.65 and time_since_slept <= 6:
        return 1  # Drink coffee for alertness boost and work

    # Short bouts of leisure for relaxation
    if intoxication < 0.05 and hypertension < 0.15 and alertness >= 0.8 and work_done < 0.5:
        return 2  # Drink beer when in a good health state for leisure

    return 0  # Default to just work when health and alertness are stable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize reducing health risks
    if hypertension > 0.012 or intoxication > 0.15:
        return 3  # sleep if any severe health risks are present
    if time_since_slept >= 8:
        return 3  # ensure regular sleep if it's been too long
    if alertness < 0.4:
        return 3  # prioritize sleep for better alertness
    if alertness < 0.6 and hypertension < 0.008 and intoxication < 0.08:
        return 1  # allow coffee to boost alertness if conditions are moderately ok
    return 0  # focus on work if all conditions are acceptable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
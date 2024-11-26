import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Ensure critical health conditions are addressed first
    if hypertension > 0.07 or intoxication > 0.3:
        return 3  # Immediate sleep needed

    # Balance productivity with health concerns and rest needs
    if time_since_slept >= 8 or alertness < 0.4:
        return 3  # Prioritize sleep to maintain health

    # Use coffee strategically to maintain alertness
    if alertness < 0.6:
        if intoxication < 0.15:  # Ensure intoxication is reasonable
            return 1  # Coffee and work to boost performance

    # Opt for work when conditions are optimal
    if alertness >= 0.6 and intoxication < 0.1:
        return 0  # Safely focus on work

    return 0  # Default to safe work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
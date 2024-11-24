import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if severely sleep-deprived or critical health indicators
    if time_since_slept > 6 or hypertension > 0.35 or intoxication > 0.25:
        return 3
    # Use coffee judiciously for moderate alertness and manageable health
    if alertness < 0.6 and hypertension <= 0.15 and intoxication <= 0.1:
        return 1
    # Work when alertness is high and health is stable
    if alertness >= 0.7 and hypertension <= 0.1 and intoxication <= 0.05:
        return 0
    # If alert or intoxicated, but health non-critical, maintain work or consider relaxation
    return 2 if intoxication < 0.2 else 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
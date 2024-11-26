import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Critical health management: Sleep based on stricter thresholds
    if hypertension > 0.025 or intoxication > 0.03:
        return 3
    if time_since_slept > 5:
        return 3

    # Caffeine boost when alertness is low with slightly relaxed health checks
    if alertness < 0.6 and hypertension < 0.02 and intoxication < 0.02:
        return 1

    # Encourage working when alertness is optimal and health is stable
    if alertness >= 0.75 and hypertension < 0.012 and intoxication < 0.012:
        return 0

    # Ensuring periodic rest after significant work completion
    if work_done > 10 and time_elapsed > 20:
        return 3

    # Default to working to maximize productivity if health conditions allow
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
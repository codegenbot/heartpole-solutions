import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if health status is critical
    if hypertension > 0.7 or intoxication > 0.5:
        return 3  # Critical: Sleep immediately

    # Focus on rest if exhaustion is imminent
    if time_since_slept > 16 or alertness < 0.3:
        return 3  # Sleep is necessary

    # Use coffee cautiously if it will improve alertness without overriding health
    if alertness < 0.5 and hypertension < 0.5:
        if time_elapsed <= 10:
            return 1  # Coffee for boosting energy early in the period

    # Keep working effectively if all health indicators are optimal and work is pending
    if alertness >= 0.5 and work_done < 1.0:
        return 0  # Work if nothing critical

    # Ensure rest after significant alertness drop
    if alertness < 0.6:
        return 3

    # Final default action when other conditions aren't strongly present
    return 3 if time_since_slept > 14 else 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
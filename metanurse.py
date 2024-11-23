import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for critical health issues
    if hypertension > 0.5 or intoxication > 0.3:
        return 3  # Sleep

    # Sleep if severely lacking rest
    if alertness < 0.5 or time_since_slept > 14:
        return 3  # Sleep

    # Use coffee strategically for increased alertness if not too late or too much work done
    if alertness < 0.7 and time_elapsed < 10 and work_done < 0.3:
        return 1  # Drink coffee and work

    # Opt for sleep if nearing end of day and alertness is low
    if time_elapsed >= 16 and alertness < 0.7:
        return 3  # Sleep

    # Work if all health metrics are safe and alertness is sufficient
    if alertness >= 0.75 and hypertension < 0.25 and intoxication < 0.15:
        return 0  # Just work

    # Default to safe option which is sleep if not absolutely clear
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)
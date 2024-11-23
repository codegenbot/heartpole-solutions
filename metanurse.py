import sys

for line in sys.stdin:
    (
        alertness,
        hypertension,
        intoxication,
        time_since_slept,
        time_elapsed,
        work_done,
    ) = map(float, line.split())

    if hypertension > 0.4 or intoxication > 0.3 or time_since_slept > 10:
        print(3)  # sleep
    elif alertness < 0.5 and hypertension < 0.25:
        print(1)  # drink coffee and work
    elif alertness >= 0.7 and hypertension < 0.25 and intoxication < 0.1:
        print(0)  # just work
    elif 0.15 <= intoxication < 0.25:
        print(2)  # drink beer and work
    else:
        print(3)  # fallback to sleep for uncertain situations
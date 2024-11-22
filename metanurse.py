import sys


def main():
    for _ in range(1000):
        observations = list(map(float, sys.stdin.readline().strip().split()))
        (
            alertness,
            hypertension,
            intoxication,
            time_since_slept,
            time_elapsed,
            work_done,
        ) = observations

        if time_since_slept > 12 or hypertension > 80 or intoxication > 0.5:
            print(3)  # Sleep
        elif alertness < 0.5 and time_since_slept > 6:
            print(1)  # Drink coffee and work
        elif alertness < 0.3 and time_since_slept > 8:
            print(2)  # Drink beer and work
        else:
            print(0)  # Just work


if __name__ == "__main__":
    main()
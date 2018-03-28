import argparse
import sys
import time
parser = argparse.ArgumentParser(description="Some print.")
parser.add_argument('--n', help='The number of the iterations.', type=int, default=10)
def main():
    args = parser.parse_args()
    for i in range(args.n):
        time.sleep(1)
        print(i)
    return 0
if __name__ == "__main__":
        sys.exit(main())

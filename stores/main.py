import json
import sys
from collections import Counter


def main():
    try:
        with open('input.txt') as fp:
            stats = json.load(fp)
    except FileNotFoundError:
        print('No source file (`input.txt`)', file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f'can\'t decode source file: {e}', file=sys.stderr)
        sys.exit(1)

    total = Counter()
    for single in stats.values():
        for name, count in single.items():
            total[name] += count
    with open('output.txt', 'w') as fp:
        json.dump(total, fp)


if __name__ == '__main__':
    main()

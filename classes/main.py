import sys


def main():
    try:
        with open('input.txt') as fp:
            data = []
            for line in fp:
                try:
                    data.append(parse_line(line))
                except ValueError as e:
                    print(f'malformed data: {e}', file=sys.stderr)
                    sys.exit(1)
    except FileNotFoundError:
        print('file `input.txt` is not found', file=sys.stderr)
        sys.exit(1)

    classLists = {}
    for name, subjectList in data:
        for subject in subjectList:
            classLists[subject] = classLists.get(subject, []) + [name]

    subject = input('Course name> ')
    if subject in classLists:
        print(f'following students are taking this course:')
        for name in classLists[subject]:
            print(f'\t{name}')
    else:
        print('Course doesn\'t exist')


def parse_line(line: str) -> tuple[str, list[str]]:
    name, subjects = line.split(':')
    name = name.strip()
    subjects = [sub.strip() for sub in subjects.split(',')]
    return name, subjects


if __name__ == '__main__':
    main()

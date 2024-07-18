import sys


def main():
    minPopulation = int(input('minimal population> '))
    try:
        with open('cities.txt') as fp:
            cities = [(name.strip(), int(population.strip())) for name, population in [line.split(':') for line in fp if ':' in line]]
    except FileNotFoundError:
        print('no source file (`cities.txt`)', file=sys.stderr)
        sys.exit(1)

    cities = [i for i in cities if i[1] > minPopulation]
    cities.sort(key=lambda i: i[0])

    with open('filtered_cities.txt', 'w') as fp:
        fp.writelines([f'{i[0]}:{i[1]}\n' for i in cities])


if __name__ == '__main__':
    main()

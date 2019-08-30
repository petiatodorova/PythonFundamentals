magic_number = int(input())

for c1 in range(1, 10):
    for c2 in range(1, 10):
        for c3 in range(1, 10):
            for c4 in range(1, 10):
                for c5 in range(1, 10):
                    for c6 in range(1, 10):
                        if c1 * c2 * c3 * c4 * c5 * c6 == magic_number:
                            print(f'{c1}{c2}{c3}{c4}{c5}{c6} ', end="")
c = 0

while True:
    d = str(input('já dormi? '))

    if d == 'sim':
        break

    c += 1
    print(f'Carneirinho {c}...')


print(f'você contou {c} carneirinhos antes de dormir. ')
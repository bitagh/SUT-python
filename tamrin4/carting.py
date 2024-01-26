def main():
    try:
        lines = [input() for _ in range(6)]

        name_1, name_2 = lines[0].split(' ')
        name_2 = name_2.strip()
        health_1, health_2 = map(int, lines[1].split(' '))
        damage_A, damage_B, damage_C = map(int, lines[2].split(' '))
        cards_damage = {'A': damage_A, 'B': damage_B, 'C': damage_C}
        p1_points, p2_points = 0, 0

        for i in range(3, 6):
            tmpcardp1, tmpcardp2 = lines[i].split(' ')
            if cards_damage[tmpcardp1[0]] > cards_damage[tmpcardp2[0]]:
                p1_points += 1
            elif cards_damage[tmpcardp2[0]] > cards_damage[tmpcardp1[0]]:
                p2_points += 1
            health_1 -= cards_damage[tmpcardp2[0]]
            health_2 -= cards_damage[tmpcardp1[0]]

        print(f"{name_1} -> Score: {p1_points}, Health: {health_1}\n{name_2} -> Score: {p2_points}, Health: {health_2}")

    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    main()

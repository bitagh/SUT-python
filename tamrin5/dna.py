class MrKrabs:
    def __init__(self, dna):
        self.dna = dna

    def modify_dna(self):
        self.dna = self.dna.replace('tt', 'o')
        return self.dna


class SpongeBob:
    def __init__(self, dna):
        self.dna = dna

    def sort_dna(self):
        return int(''.join(sorted(str(len(self.dna)))))


class Octopus:
    def __init__(self, dna):
        self.dna = dna

    def replace_triplets(self):
        new_dna = ""
        i = 0
        j = 0
        count = 0
        while i < len(self.dna):
            if self.dna[i] == 'x' and count == 0:
                j = i
                count += 1
            while (i + 3 < len(self.dna)) and (self.dna[i] == self.dna[i + 1]) and (self.dna[i] == self.dna[i + 2]):
                new_dna += "(0_0)"
                i += 3
            else:
                new_dna += self.dna[i]
                i += 1
        if j != 0:
            new_dna += str(j)
        return new_dna


def main():
    input_data = input().strip()

    if input_data.startswith("m"):
        mr_krabs = MrKrabs(input_data[1:] + input_data[:10])
        print('m' + mr_krabs.modify_dna())
    elif input_data.startswith("sb"):
        sponge_bob = SpongeBob(input_data)
        print(sponge_bob.sort_dna())
    elif input_data.startswith("s") and not input_data.startswith("sb"):
        octopus = Octopus(input_data[0:])
        print(octopus.replace_triplets())
    elif input_data.endswith('m'):
        input_data = input_data[::-1]
        mr_krabs = MrKrabs(input_data[1:] + input_data[:10])
        print('m' + mr_krabs.modify_dna())
    elif input_data.endswith('bs'):
        input_data = input_data[::-1]
        sponge_bob = SpongeBob(input_data)
        print(sponge_bob.sort_dna())
    elif input_data.endswith('s') and not input_data.endswith('bs'):
        input_data = input_data[::-1]
        octopus = Octopus(input_data[0:])
        print(octopus.replace_triplets())
    else:
        print('invalid input')


if __name__ == "__main__":
    main()

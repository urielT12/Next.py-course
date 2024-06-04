

def check_id_valid(id_number):
    """function that validate the id number that given - made in a oneLiner as asked"""
    digits_list = [int(digit) for digit in str(id_number)]
    sum_of_digits = sum([int(x/10) + int(x%10) if x > 9 else x for x in [x * 2 if (i % 2 != 0) else x for i,x in enumerate(digits_list)]])

    if sum_of_digits % 10:
        return False
    return True


class IDIterator:
    """an iterator class"""
    def __init__(self,id):
        self._id = id

    def __iter__(self):
        return self

    def __next__(self):
        """iterate from self._id to 999999999 and returns only the valid ids"""
        self._id += 1
        while self._id < 999999999:
            if check_id_valid(self._id):
                return self._id
            self._id += 1
        raise StopIteration()

def id_generator(id_number):
    """iterate from given id to 999999999 and returns only the valid ids"""
    id_number += 1
    while id_number < 999999999:
        if check_id_valid(id_number):
            yield id_number
        id_number += 1



def main():
    """a main program that generates 10 valid ids from a given ID - user can choose between generator and iterator"""
    id = input("Enter ID: ")
    it_or_gen = input("Generator or Iterator? (gen/it)? ")
    if it_or_gen == "gen":
        id_gen = id_generator(int(id))
        for i in range(10):
            print(next(id_gen))
    elif it_or_gen == "it":
        id_iterator = IDIterator(int(id))
        valid_ids = []
        for i in range(10):
            try:
                valid_ids.append(next(id_iterator))
            except StopIteration:
                break

        for valid_id in valid_ids:
            print(valid_id)



if __name__ == '__main__':
    main()

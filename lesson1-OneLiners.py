import os

path = "C:\\Users\\uriel\\OneDrive\\מסמכים\\names.txt"
def longest_name_in_file(path):
    """prints the longest name that in the file"""
    with open(path,'r') as file:
        print(max(file,key=len).strip())


def sum_of_names_length(path):
    """prints the sum of all the names length"""
    with open(path,'r') as file:
        print(sum(len(line.strip()) for line in file))


def print_shortest_names(path):
    """going through the file and prints the shortest name"""
    with open(path,'r') as file:
        lines = file.readlines()
        min_length = min(len(line.strip()) for line in lines)
        print('\n'.join(line.strip() for line in lines if len(line.strip()) == min_length))


def new_length_file(path):
    """create a new file and adds the names length in place of each name
    used os module because of a permissions problem"""
    with open(path, 'r') as file:
        with open(os.path.join(os.path.expanduser('~'), 'name_length.txt'),'w') as new_file:
                new_file.write('\n'.join([str(len(line.strip())) for line in file]))



def all_words_in_length(path):
    """receives from the user a number representing the length of a name and
    prints all the names in the names.txt file that are of this length"""
    with open(path,'r') as file:
        length = input("Enter name length: ")
        print('\n'.join(line.strip() for line in file if len(line.strip()) == int(length)))


def main():
    print("longest name: ")
    longest_name_in_file(path)
    print("sum of lengths: ")
    sum_of_names_length(path)
    print(("shortest names: "))
    print_shortest_names(path)
    print("a new length file created")
    new_length_file(path)
    all_words_in_length(path)




if __name__ == '__main__':
    main()


"""
output:
    longest name: 
    Vladimir
    sum of lengths: 
    38
    shortest names: 
    Ed
    Jo
    a new length file created
    Enter name length: 4
    Hans
    Anna
"""

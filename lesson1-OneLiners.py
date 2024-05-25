import os


def longest_name_in_file(path):
    with open(path,'r') as file:
        print(max(file,key=len).strip())


def sum_of_names_length(path):
        with open(path,'r') as file:
            print(sum(len(line.strip()) for line in file))


def print_shortest_names(path):
    with open(path,'r') as file:
        lines = file.readlines()
        min_length = min(len(line.strip()) for line in lines)
        print('\n'.join(line.strip() for line in lines if len(line.strip()) == min_length))


def new_length_file(path):
    with open(path, 'r') as file:
        with open(os.path.join(os.path.expanduser('~'), 'name_length.txt'),'w') as new_file:
                new_file.write('\n'.join([str(len(line.strip())) for line in file]))


def all_words_in_length(path):
    with open(path,'r') as file:
        length = input("Enter name length: ")
        print('\n'.join(line.strip() for line in file if len(line.strip()) == int(length)))






new_length_file("C:\\Users\\uriel\\OneDrive\\מסמכים\\names.txt")
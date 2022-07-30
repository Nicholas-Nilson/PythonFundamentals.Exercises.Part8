import os

target_path = "/Users/nick/Python/Labs/PythonFundamentals.Exercises.Part8/"


def get_folder_name(path):
    list = path.split("/")
    last_index = len(list) - 2
    return str(list[last_index])


# def create_file(file_name):
#     file =  open(file_name + ".txt", "x")
#     return "{}.txt".format(file_name)

# def open_file(file_name):


def write_tree(path):
    list = []
    for root, directory, files in os.walk(path):
        for item in files:
            list.append(root + item)
    return list


def write_to_file(file_name, list_to_write):
    f = open("{}".format(file_name) + ".txt", "a")
    for item in list_to_write:
        f.write(item + "\n")



# get name of directory we're searching files & subdirectories for, to abstract
# the naming of the new file.
new_file_name = get_folder_name(target_path)

#populate a list with things to write
tree_list = write_tree(target_path)
print(tree_list)

# write to file & close
write_to_file(new_file_name, tree_list)

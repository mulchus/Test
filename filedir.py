import os


def get_total_size(folder_path):
    return sum(
        sum(os.path.getsize(os.path.join(path, file)) for file in files)
        for path, _, files in os.walk(folder_path)
    )


def file_tree(folder_path):
    for path, _, files in os.walk(folder_path):
        for file in files:
            yield file

    # return (file for file in (files for path, _, files in os.walk(folder_path)))
    # yield from (file for file in (files for path, _, files in os.walk(folder_path)))
    # yield from (f for f in (file for file in (files for path, _, files in os.walk(folder_path))))
    # return (f for f in (file for file in (files for path, _, files in os.walk(folder_path))))
    # return (file for file in (files for path, _, files in os.walk(folder_path)))


folder_path = 'd://Python/Test'
new_generator = file_tree(folder_path)
for file in new_generator:
    print(file)
    # for f in file:
    #     print(f)


if __name__ == '__main__':
    import sys
    # folder_path = sys.argv[-1]
    # folder_path = 'd://Python/Test'
    # print(get_total_size(folder_path))

    # new_generator = file_tree(folder_path)
    # for file in new_generator:
    #     print(file)

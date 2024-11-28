from dataclasses import dataclass
from typing import Optional

def load_file(file_path: str):
    with open(file_path) as file:
        content = file.readlines()

    return content

@dataclass
class Directory:
    parent: str
    sub_directories: Optional[list[str]] = None
    size_of_files: int = 0
    total_size: int = 0

    def add_filesize(self, size: int):
        self.size_of_files += size

    def add_subdirectory(self, dir_name: str):
        if self.sub_directories is None:
            self.sub_directories = [dir_name]
        else:
            self.sub_directories.append(dir_name)

def compute_total_sizes(file_system, folder) -> int:
    current_folder = file_system[folder]
    total_size = current_folder.total_size
    if total_size != 0:
        return total_size

    total_size += current_folder.size_of_files
    if current_folder.sub_directories is not None and len(current_folder.sub_directories) != 0:
        for sub_folder in current_folder.sub_directories:
            total_size += compute_total_sizes(file_system, sub_folder)

    return total_size


def create_file_tree(task_input: list[str]) -> dict[str, Directory]:
    current_path = ""
    file_tree =  {}
    for line in task_input:
        command = line.strip().split()
        #print(command)
        if command[0] == '$':
            if command[1] == 'cd':
                target = command[2]
                if target == '/':
                    current_path = "/"
                    if current_path not in file_tree:
                        file_tree[current_path] = Directory(parent="")
                elif target == '..':
                    current_path = file_tree[current_path].parent
                else:
                    current_path += target + "/"
        #        print(current_path)
        elif command[0] == 'dir':
            folder_path = current_path + command[1] + "/"
            entry = Directory(parent=current_path)
            file_tree[current_path].add_subdirectory(folder_path)
            file_tree[folder_path] = entry
        #    print(entry)
        else:
            file_tree[current_path].add_filesize( int(command[0]))
    return file_tree


def part_01(task_input: list[str]) -> int:
    result = 0
    file_tree = create_file_tree(task_input)

    print(file_tree)
    # compute total sizes
    for key in file_tree.keys():
        total_size = compute_total_sizes(file_tree, key)
        file_tree[key].total_size = total_size
        if total_size < 100000:
            result += total_size

    print(file_tree)
    # put logic here
    return result


def part_02(task_input: list[str]) -> int:
    result = 0
    max_size = 7e7
    target_size = 3e7
    candidates = []

    file_tree = create_file_tree(task_input)

    for key in file_tree.keys():
        total_size = compute_total_sizes(file_tree, key)
        file_tree[key].total_size = total_size

    free_size = max_size - file_tree['/'].total_size

    for key, value in file_tree.items():
        if free_size + value.total_size > target_size:
            candidates.append((key, value.total_size))

    candidates.sort(key=lambda x: x[1])

    print(candidates)

    result = candidates[0][1]

    # put logic here
    return result


if __name__ == '__main__':
    result_part1 = part_01(load_file('./input'))
    print(f"Outcome of part 1 is: {result_part1}.")
    result_part2 = part_02(load_file('./input'))
    print(f"Outcome of part 2 is: {result_part2}.")

def test_part1():
    content = load_file('./tests/input')
    result = part_01(content)
    # put test result here
    assert result == 95437

def test_part2():
    content = load_file('./tests/input')
    result = part_02(content)
    # put test result here
    assert result == 24933642

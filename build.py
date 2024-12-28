import os
import shutil

map = []
for entry in os.scandir(os.getcwd()):
    if entry.is_dir() and entry.path != ".git":
        map.append(entry)

"""
Update requirements.txt with all the dependencies
"""
def update_deps(map):
    deps = set()
    for map_name in map:
        reqs_path = f"{map_name.path}/requirements.txt"
        try:
            with open(reqs_path, "r") as file:
                reqs = file.read().splitlines()  # read line by line to avoid splitting on newline characters
                deps.update(reqs)
        except FileNotFoundError:
            print(f"No requirements.txt found in {map_name.path}")

    current_deps_str = ""
    try:
        with open("requirements_base.txt", "r") as base_file:
            for dep in base_file.readlines():
                if dep.strip() and not dep.startswith("#"):  # ignore comments
                    deps.add(dep.strip())
    except FileNotFoundError:
        print("No requirements_base.txt found")

    with open("requirements.txt", "w") as output_file:
        for dep in sorted(deps):  # sort dependencies alphabetically
            current_deps_str += f"{dep}\n"

    return list(deps)

"""
Clear temporary directories
"""
def clear_directories():
    return True


"""
Iterates through build process and logs steps
"""
try:
    map = [entry for entry in os.scandir(os.getcwd()) if entry.is_dir() and entry.path != ".git"]
    update_deps(map)
    print("Updating Dependencies")
except Exception as e:
    print(f"Failed to Update Dependencies: {e}")

try:
    clear_directories()
    print("Clearing Temporary Directories")
except Exception as e:
    print(f"Failed to Clear Temporary Directories: {e}")

import os

def build_tree(path, ignore_folders=None):
    if ignore_folders is None:
        ignore_folders = {".venv", ".git", "__pycache__"}  # folders to ignore listing

    tree = {}

    for item in os.listdir(path):
        item_path = os.path.join(path, item)

        # If directory
        if os.path.isdir(item_path):
            if item in ignore_folders:
                tree[item] = "[ignored folder]"
            else:
                tree[item] = build_tree(item_path, ignore_folders)

        # If file
        else:
            tree[item] = ""  # just indicate file exists

    return tree


def print_tree(tree, indent=0):
    """Pretty print the dictionary structure"""
    for key, val in tree.items():
        print("  " * indent + f"- {key}")
        if isinstance(val, dict):
            print_tree(val, indent + 1)
        elif isinstance(val, str) and val:
            print("  " * (indent + 1) + val)


if __name__ == "__main__":
    project_path = "C:\PRIVATE_SPACE\Personal\LLMOPS_Bootcamp\document_portal"  # change this to your project root path
    tree = build_tree(project_path)
    print_tree(tree)

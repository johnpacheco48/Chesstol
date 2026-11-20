import os
import shutil
import argparse

from textnode import TextNode, TextType
from generate_page import generate_pages_recursive


def main():
    ##arg parser for "import dir" "export dir"
    parser = argparse.ArgumentParser(description="DirectoryMover")
    parser.add_argument("source_dir", type=str, help="Source Directory")
    parser.add_argument("target_dir", type=str, help="Target Directory")
    args = parser.parse_args()
    source = args.source_dir
    target = args.target_dir
    ##setup paths for directories and check if source is valid
    source_dir = os.path.abspath(source)
    target_dir = os.path.abspath(target)
    print(source_dir, target_dir)
    if os.path.isdir(source_dir) is False:
        raise ValueError(f"{source_dir} is not a valid directory")
    #copy from source to target
    print(f"Moving files from {source_dir} to {target_dir}...")
    os.makedirs(target_dir, exist_ok=True)
    copy_dir(source_dir, target_dir)
    os.makedirs(source_dir)
    #generate page
    generate_pages_recursive("content", "template.html", "public")



def copy_dir(source_dir: str, target_dir: str) -> None:
    for file in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file)
        if os.path.isdir(file_path):
            source_file = os.path.join(source_dir, file)
            target_file = os.path.join(target_dir, file)
            print(f"Extracting files from {file}...")
            os.makedirs(target_file, exist_ok=True)
            copy_dir(source_file, target_file)
        else:
            shutil.copy(file_path, target_dir)
            print(f"Moved {file} to {target_dir}")
    shutil.rmtree(source_dir)

main()

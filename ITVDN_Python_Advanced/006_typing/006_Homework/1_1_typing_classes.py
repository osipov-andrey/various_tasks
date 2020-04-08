from typing import List


class Directory:

    def __init__(
            self,
            name: str,
            files: List['File'] = None,
            sub_directories: List['Directory'] = None,
            root: 'Directory' = None,
    ):
        self.name = name
        self.root = root
        self.files = files or []
        self.sub_directories = sub_directories or []

    def add_sub_directory(self, directory: 'Directory'):
        self.sub_directories.append(directory)
        directory.root = self

    def remove_sub_directory(self, directory: 'Directory'):
        self.sub_directories.remove(directory)
        directory.root = None

    def add_file(self, file: 'File'):
        self.files.append(file)
        file.directory = self

    def remove_file(self, file: 'File'):
        self.files.remove(file)
        file.directory = None

    def __repr__(self):
        return f"Dir: {self.name}"


class File:
    def __init__(
            self,
            name: str,
            directory: Directory = None
    ):
        self.name = name
        self.directory = directory

    def __repr__(self):
        return f"File: {self.name}"

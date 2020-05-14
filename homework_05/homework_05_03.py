class File:
    def __init__(self, name, method):
        self._file = open(name, method)

    def __enter__(self):
        print(f"Entered file")
        return self._file

    def __exit__(self, ex_type, ex_value, ex_traceback):
        print(f"Close file")
        self._file.close()


if __name__ == '__main__':
    with File('test.txt', 'w') as _file:
        _file.write('Hello world')

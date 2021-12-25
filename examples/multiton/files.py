from ..logger import logger


class FileManagerFactory():
    open_files = {}

    def __new__(cls, path, mode):
        if path not in cls.open_files:
            cls.open_files[path] = FileContextManager(path, mode)

        return cls.open_files[path]


class FileContextManager():
    def __init__(self, path, mode):
        logger.info(f'creating Manager for {path} with {mode} rights')
        self.file = open(path, mode)
        self.n_open = 0

    def __enter__(self):
        self.n_open += 1
        logger.info(f'current opened context {self.n_open}')

        return self.file

    def __exit__(self, type, value, traceback):
        self.n_open -= 1
        logger.info(f'current opened context {self.n_open}')

        if(self.n_open == 0):
            self.file.close()

    def read(self):
        return self.file.readlines()

    def write(self):
        raise NotImplemented

from ..logger import logger


class FileManagerFactory():
    open_files = {}

    def __new__(cls, path, mode):
        if path not in cls.open_files:
            cls.open_files[path] = FileSharedContextManager(path, mode)

        return cls.open_files[path]


class FileSharedContextManager():
    def __init__(self, path, mode):
        logger.info(f'creating Manager for {path} with {mode} rights')
        self.n_opened = 0
        self.path = path
        self.mode = mode

    def __enter__(self):
        if (self.n_opened == 0):
            self.file = open(self.path, self.mode)
        self.n_opened += 1

        logger.info(f'current opened context {self.n_opened}')
        return self.file

    def __exit__(self, type, value, traceback):
        self.n_opened -= 1
        logger.info(f'current opened context {self.n_opened}')

        if(self.n_opened == 0):
            self.file.close()

    def read(self):
        return self.file.readline()

    def write(self):
        raise NotImplemented

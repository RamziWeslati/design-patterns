from ..logger import logger

from .files import FileManagerFactory


def main():
    FILE_PATH = 'examples/popular_file.txt'

    def read_file_debounced(file, caller):
        for _ in range(20):
            logger.info(f'from {caller}, : {file.read()}')
            time.sleep(1)

    with FileManagerFactory(FILE_PATH, 'r') as file_manager_1, \
            FileManagerFactory(FILE_PATH, 'r') as file_manager_2:
        thread_1 = Thread(target=read_file_debounced, args=(file_manager_1, 1))
        thread_1.start()
        thread_2 = Thread(target=read_file_debounced, args=(file_manager_2, 2))
        thread_2.start()
        thread_1.join()
        thread_2.join()


if __name__ == '__main__':
    import time
    from threading import Thread

    main()

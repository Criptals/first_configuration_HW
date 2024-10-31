import unittest
from commands import FileSystemEmulator

class TestFileSystemEmulator(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystemEmulator("path_to_zip")

    def test_ls(self):
        result = self.fs.ls("/")
        self.assertIsInstance(result, list)

    def test_cd(self):
        self.fs.cd("/some_directory")
        # Проверка текущего каталога

    def test_mv(self):
        # Проверка перемещения файла

    def test_chmod(self):
        # Проверка изменения прав доступа

if __name__ == "__main__":
    unittest.main()

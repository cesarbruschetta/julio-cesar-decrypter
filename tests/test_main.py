import unittest
from unittest.mock import patch

from jc_decrypter.main import process, main


class TestMainProcess(unittest.TestCase):
    @patch("jc_decrypter.main.decrypter")
    def test_arg_decrypter(self, mk_decrypter):

        process(["--token", "1234567890"])
        mk_decrypter.assert_called_once_with("1234567890")

    def test_not_arg(self):

        with self.assertRaises(SystemExit) as cm:
            process([])
            self.assertEqual(
                "the following arguments are required: --token/-t", str(cm.exception)
            )


class TestMainMain(unittest.TestCase):
    @patch("jc_decrypter.main.process")
    def test_main_process(self, mk_process):

        mk_process.return_value = 0
        self.assertRaises(SystemExit, main)
        mk_process.assert_called_once_with(["test"])

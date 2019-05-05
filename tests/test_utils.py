import os
import unittest
from unittest.mock import patch, ANY

from jc_decrypter.utils import files, request
from jc_decrypter.config import BASE_PATH

class TestUtilsFiles(unittest.TestCase):
    def test_write_file(self):
        expected_text = "<a><b>bar</b></a>"
        filename = "foo_test.txt"

        try:
            files.write_file(filename, expected_text)

            with open(filename, "r") as f:
                text = f.read()
        finally:
            os.remove(filename)

        self.assertEqual(expected_text, text)

    def test_write_binary_file(self):
        expected_text = b"<a><b>bar</b></a>"
        filename = "foo_test_binary.txt"

        try:
            files.write_file_binary(filename, expected_text)

            with open(filename, "rb") as f:
                text = f.read()
        finally:
            os.remove(filename)

        self.assertEqual(expected_text, text)

    def test_sha1(self):

        self.assertEqual(files.sha1("foo"), "0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33")


class TestUtilsRequest(unittest.TestCase):
    @patch("jc_decrypter.utils.request.requests")
    def test_get(self, mk_requests):

        expected = {"params": {"token": "1234567890"}}
        request.get("http://api.test.com", **expected)
        mk_requests.get.assert_called_once_with("http://api.test.com", **expected)

    @patch("jc_decrypter.utils.request.requests")
    def test_post(self, mk_requests):

        expected = {"params": {"token": "1234567890"}}
        request.post("http://api.test.com", os.path.join(BASE_PATH, "answer.json"), **expected)
       
        mk_requests.post.assert_called_once_with(
            "http://api.test.com",
            data=ANY, headers=ANY, 
            params={'token': '1234567890'}
        )
        
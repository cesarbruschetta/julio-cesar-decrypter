import unittest
from unittest.mock import patch

from jc_decrypter.processing import decrypter


class TestDecrypterProcess(unittest.TestCase):
    @patch("jc_decrypter.processing.request")
    def test_decrypter(self, mk_request):

        mk_request.get().json.return_value = {
            "numero_casas": 3,
            "token": "1234567890",
            "cifrado": "d oljhlud udsrvd pduurp vdowrx vreuh r fdfkruur fdqvdgr",
            "decifrado": "",
            "resumo_criptografico": "",
        }

        result = decrypter("1234567890")

        self.assertEqual(
            result["result_processing"]["decifrado"],
            "a ligeira raposa marrom saltou sobre o cachorro cansado",
        )

""" module to method to processing """

import os
import json
import string
import logging
from typing import Dict
from jc_decrypter.utils import request, files
from jc_decrypter import config


ALFABETO = string.ascii_lowercase
logger = logging.getLogger(__name__)


def decrypter(api_token: str) -> Dict:
    """ method to processing to descypter data from api """

    data = request.get(config.API_GENERATE_DATA, params={"token": api_token}).json()

    # Salvando Arquivo Inicial
    files.write_file(os.path.join(config.BASE_PATH, "answer.json"), json.dumps(data))

    numero_casas = data["numero_casas"]
    cifrado = data["cifrado"]
    decifrado = ""

    logger.info("Texto cifrado: %s", cifrado)
    for letra in cifrado:
        if letra in ALFABETO:
            index_letra_decifrada = ALFABETO.index(letra) - numero_casas
            try:
                decifrado += ALFABETO[index_letra_decifrada]
            except IndexError:
                decifrado += ALFABETO[index_letra_decifrada - 26]
        else:
            decifrado += letra

    logger.info("Texto decifrado: %s", decifrado)
    print(decifrado)

    data["decifrado"] = decifrado
    data["resumo_criptografico"] = files.sha1(decifrado)

    # Salvando Arquivo Final
    files.write_file(os.path.join(config.BASE_PATH, "answer.json"), json.dumps(data))

    submit_data = request.post(
        config.API_SUBMIT_DATA,
        path_to_file=os.path.join(config.BASE_PATH, "answer.json"),
        params={"token": api_token},
    ).json()

    return {"return_submit": submit_data, "result_processing": data}

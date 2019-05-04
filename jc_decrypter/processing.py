"""  """


import os
import json
import string
from jc_decrypter.utils import request, files
from jc_decrypter import config

ALFABETO = string.ascii_lowercase


def decrypter(api_token: str):
    """  """

    data = request.get(config.API_GENERATE_DATA, params={"token": api_token}).json()

    # Salvando Arquivo Inicial
    files.write_file(os.path.join(config.BASE_PATH, "answer.json"), json.dumps(data))

    numero_casas = data["numero_casas"]
    cifrado = data["cifrado"]
    decifrado = ""

    for letra in cifrado:

        if letra in ALFABETO:
            index_letra_decifrada = ALFABETO.index(letra) - numero_casas
            try:
                decifrado += ALFABETO[index_letra_decifrada]
            except IndexError:
                decifrado += ALFABETO[index_letra_decifrada - 26]

        else:
            decifrado += letra

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

    print(submit_data)

    return submit_data

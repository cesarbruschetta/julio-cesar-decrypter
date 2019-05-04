"""  """

import logging
import hashlib

logger = logging.getLogger(__name__)


def write_file(path, source, mode="w"):
    logger.debug("Gravando arquivo: %s", path)
    with open(path, mode, encoding="utf-8") as f:
        f.write(source)


def write_file_binary(path, source):
    logger.debug("Gravando arquivo binario: %s", path)
    with open(path, "wb") as f:
        f.write(source)


def sha1(mensagem):
    _sum = hashlib.sha1()
    _sum.update(mensagem.encode("utf-8"))
    return _sum.hexdigest()

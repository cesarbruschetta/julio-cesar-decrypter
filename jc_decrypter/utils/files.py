""" module utils to method to files """

import logging
import hashlib

logger = logging.getLogger(__name__)


def write_file(path: str, source: str, mode="w") -> None:
    """ write file in file system in unicode """
    logger.debug("Gravando arquivo: %s", path)
    with open(path, mode, encoding="utf-8") as f:
        f.write(source)


def write_file_binary(path: str, source: bytes) -> None:
    """ write file in file system in bytes """
    logger.debug("Gravando arquivo binario: %s", path)
    with open(path, "wb") as f:
        f.write(source)


def sha1(mensagem: str) -> str:
    """ generate sha1 hash """
    _sum = hashlib.sha1()
    _sum.update(mensagem.encode("utf-8"))
    return _sum.hexdigest()

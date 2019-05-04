""" modulo utils to request methods """

import os
import requests
import logging

logger = logging.getLogger(__name__)


def get(uri: str, **kwargs):

    r = requests.get(uri, **kwargs)
    r.raise_for_status()
    return r


def post(uri: str, path_to_file: str, **kwargs):

    headers = {
        "content-type": "multipart/form-data",
        "Content-Type": "application/json",
    }
    # files = {"answer": open(path_to_file, "rb")}
    r = requests.post(uri, files={"answer": path_to_file}, headers=headers, **kwargs)
    r.raise_for_status()

    return r

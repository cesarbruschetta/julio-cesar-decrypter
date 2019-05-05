""" modulo utils to request methods """

import os
import requests
import logging
from requests_toolbelt import MultipartEncoder


logger = logging.getLogger(__name__)


def get(uri: str, **kwargs) -> requests.Request:

    r = requests.get(uri, **kwargs)
    r.raise_for_status()
    return r


def post(uri: str, path_to_file: str, **kwargs) -> requests.Request:

    m = MultipartEncoder(
        fields={
            "answer": (
                os.path.basename(path_to_file),
                open(path_to_file, "rb"),
                "application/json",
            )
        }
    )
    r = requests.post(uri, data=m, headers={"Content-Type": m.content_type}, **kwargs)
    r.raise_for_status()

    return r

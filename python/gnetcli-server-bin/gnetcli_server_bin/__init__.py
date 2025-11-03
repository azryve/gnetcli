import os
from importlib.resources import files

def get_binary_path() -> str:
    """
    Return the absolute path to the packaged gnetcli_server binary.
    """
    name = "gnetcli_server.exe" if os.name == "nt" else "gnetcli_server"
    return str(files(__package__).joinpath("_bin", name))

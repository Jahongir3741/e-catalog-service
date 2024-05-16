from uuid import uuid4


def poster_directory_path(instance: str, filename: str):
    lst = filename.split('.')
    return f"poster/{uuid4()}.{lst[-1]}"


def cadre_directory_path(instance: str, filename: str):
    lst = filename.split('.')
    return f"cadre/{uuid4()}"

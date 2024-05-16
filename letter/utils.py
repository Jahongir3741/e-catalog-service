from uuid import uuid4


def file_directory_path(instance, filename):
    return f"letter/{uuid4()}"

import uuid


def random_suffix():
    return uuid.uuid4().hex[:6]

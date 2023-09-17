# NOQA: D100

__all__ = ["hello_world"]

HELLO_WORLD_MSG = "Hello, World!"
HELLO_WORLD_TPL = "Hello, %s!"


def hello_world(name=None):
    """Return a "Hello, World!" message.
    """
    if name is None:
        return HELLO_WORLD_MSG
    else:
        return HELLO_WORLD_TPL % name

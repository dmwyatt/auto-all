"""
Auto-All package

auto_all can be used for controlling what is made available
for import from a package.

Example usage:

    First, import the auto_all functions.

        >>> from auto_all import start_all, end_all

    If your package has external dependencies then these can be imported
    and the imported objects can be hidden.  In this case we will import
    pathlib.Path and show that it doesn't appear on the __all__ list.

        >>> from pathlib import Path

    Now we can define some internal functions that we want to keep private.
    We can also do this using underscore prefixes, but auto_all gives us a
    little more control.

        >>> def a_private_function():
        ...     print("This is a private function.")

    Now we are ready to start defining public functions, so we use
    ``start_all()``.  We need to pass it the globals dict so that it can
    see what's already defined.

        >>> start_all(globals())

    Now we can define our public functions.

        >>> def a_public_function():
        ...     print("This is a public function.")

    Finally we use ``end_all()`` to finish defining public functions and
    create the ``__all__`` variable.

        >>> end_all(globals())

    When we look at the ``__all__`` variable we can see only the public
    facing function is listed.

        >>> print(__all__)
        ['a_public_function']

"""
_GLOBAL_VAR_NAME = '_do_not_include_all'


def start_all(globs):
    globs[_GLOBAL_VAR_NAME] = list(globs.keys()) + [_GLOBAL_VAR_NAME]


def end_all(globs):
    globs['__all__'] = list(
        set(list(globs.keys())) - set(globs[_GLOBAL_VAR_NAME])
    )

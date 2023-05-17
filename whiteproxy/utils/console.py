from typing import Any
import click


def print_warning(message: str,
                  *args: Any,
                  **kwargs: Any) -> None:
    return click.secho(message, *args, fg='yellow', **kwargs)


def print_success(message: str,
                  *args: Any,
                  **kwargs: Any) -> None:
    return click.secho(message, *args, fg='green', **kwargs)


def print_error(message: str,
                *args: Any,
                **kwargs: Any) -> None:
    return click.secho(message, *args, fg='red', **kwargs)


def print_exception(e: Exception) -> None:
    print_error(f'{e.__class__.__name__}: {str(e)}')

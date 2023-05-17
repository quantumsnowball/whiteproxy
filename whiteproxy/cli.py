import click
from subprocess import Popen

from whiteproxy.utils.console import print_warning


@click.command()
@click.option('-s', '--src', required=True, help='proxy source socket')
@click.option('-d', '--dest', required=True, help='proxy destination socket')
@click.option('-a', '--allow', required=True, multiple=True, help='whitelist ip addresses')
@click.argument('command', nargs=-1, type=str)
def whiteproxy(src: str,
               dest: str,
               allow: list[str],
               command: str) -> None:
    '''
    Run COMMAND and proxy serve the service
    (use `--` as prefix if COMMAND uses its own options)
    '''
    print_warning(src)
    print_warning(dest)
    print_warning(', '.join(allow))

    print_warning(' '.join(command))
    process = Popen(command)
    process.wait()

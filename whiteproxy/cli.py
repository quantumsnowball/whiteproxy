import click

import asyncio
from whiteproxy.utils.console import print_warning


async def async_exec(command: str, *args: str) -> None:
    proc = await asyncio.create_subprocess_exec(command, *args)
    await proc.wait()


@click.command()
@click.option('-s', '--src', metavar='IP:PORT', required=True, help='proxy source socket')
@click.option('-d', '--dest', metavar='IP:PORT', required=True, help='proxy destination socket')
@click.option('-a', '--allow', required=True, multiple=True, help='whitelist ip addresses')
@click.argument('command', nargs=1, type=str)
@click.argument('args', nargs=-1, type=str)
def whiteproxy(src: str,
               dest: str,
               allow: list[str],
               command: str,
               args: list[str]) -> None:
    '''
    Run COMMAND and proxy serve the service
    (use `--` as prefix if COMMAND uses its own options)
    '''
    print_warning(src)
    print_warning(dest)
    print_warning(', '.join(allow))

    print_warning(f'{command} {" ".join(args)}')
    asyncio.run(async_exec(command, *args))

import click

import asyncio
from asyncio import StreamReader, StreamWriter
from whiteproxy.utils.console import print_warning


async def start_target(command: str,
                       *args: str) -> None:
    # start subprocess
    proc = await asyncio.create_subprocess_exec(command, *args)
    print_warning(f'{command} {" ".join(args)}')
    await proc.wait()


async def start_proxy(host: str,
                      target: str) -> None:
    # src and dest socket
    host_addr, host_port = host.split(':')
    target_addr, target_port = target.split(':')
    print_warning(f'Redirect: {host_addr}:{host_port} -> {target_addr}:{target_port}')

    # server
    async def serve(reader: StreamReader, writer: StreamWriter) -> None:
        # confirm ip is in whitelist
        # TODO
        addr, port = writer.get_extra_info('peername')
        print(f'Incoming: {addr}:{port}')

        while True:
            print('reading... ')
            data = await reader.read(1024)
            if not data:
                break

        print('ended.')
        # await async_exec(command, *args)
        # start proxy redirection
        # TODO

    server = await asyncio.start_server(serve, host_addr, host_port, limit=1)
    async with server:
        await server.serve_forever()


@click.command()
@click.option('-h', '--host', metavar='IP:PORT', required=True, help='proxy host socket')
@click.option('-t', '--target', metavar='IP:PORT', required=True, help='proxy target socket')
@click.option('-a', '--allow', required=True, multiple=True, help='whitelist ip addresses')
@click.argument('command', nargs=1, type=str)
@click.argument('args', nargs=-1, type=str)
def whiteproxy(host: str,
               target: str,
               allow: list[str],
               command: str,
               args: list[str]) -> None:
    '''
    Run COMMAND and proxy serve the service
    (use `--` as prefix if COMMAND uses its own options)
    '''
    async def tasks() -> None:
        await asyncio.gather(
            asyncio.create_task(start_target(command, *args)),
            asyncio.create_task(start_proxy(host, target)),
        )
    asyncio.run(tasks())

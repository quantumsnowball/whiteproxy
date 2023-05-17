import click


@click.command()
@click.option('-s', '--src', required=True, help='proxy source socket')
@click.option('-d', '--dest', required=True, help='proxy destination socket')
@click.option('-a', '--allow', required=True, multiple=True, help='whitelist ip addresses')
def whiteproxy(src: str,
               dest: str,
               allow: list[str]) -> None:
    print(src)
    print(dest)
    print(allow)

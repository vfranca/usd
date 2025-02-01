"""
Converte USD para BRL
"""

import click


@click.command()
@click.argument("preco", type=float)
@click.option("--cambio", "-c", type=float, default=6.00)
def usd(preco, cambio):
    """Converte USD para BRL

    parametros:
    preco (float): preco em USD
    cambio (float): taxa de cambio

    resultado:
    float: preco em BRL"""
    brl = preco * cambio
    click.echo("BRL %.2f" % brl)


if __name__ == "__main__":
    usd()

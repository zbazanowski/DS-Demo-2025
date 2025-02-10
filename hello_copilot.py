import click

'''
This is a simple script that takes a name as input and prints a greeting message.
'''


@click.command()
@click.option('--name', prompt='Your name', help='The person to greet.')
def hello(name):
    click.echo(f'Hello {name}!')

if __name__ == '__main__':
    hello()


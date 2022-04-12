'''toy example for click'''

import click

@click.command()
@click.option('--phrase', prompt='Enter a phrase', help = 'Type anything')

def tokenize(phrase):
    '''tokenizing the phras'''

    click.echo(f'tokenized phrase: {phrase.split()}')

if __name__ == '__main__':
    tokenize()

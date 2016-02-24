# -*- coding: utf-8 -*-
import getpass

import click

import kindle
import services


@click.command()
@click.option('--kindledb', default='vocab.db', help='.db file from Kindle')
@click.option('--lingualeo-email', help='LinguaLeo email')
def export(kindledb, lingualeo_email):
    password = getpass.getpass('LinguaLeo password:')

    words = kindle.read_words(kindledb)

    lingualeo = services.LinguaLeo(lingualeo_email, password)
    lingualeo.auth()

    for word_info in words:
        translate = lingualeo.get_translate(word_info['text'])
        if translate['is_exist']:
            print 'Already exists: %s' % word_info['text']
        else:
            lingualeo.add_word(word_info['text'], translate['translated_word'], word_info['context'])
            print 'Added word: %s' % word_info['text']


if __name__ == '__main__':
    export()

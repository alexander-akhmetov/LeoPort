# -*- coding: utf-8 -*-
import sqlite3


def read_words(database_name):
    words = []
    conn = sqlite3.connect(database_name)
    sql = (
        'SELECT word, usage from words '
        'LEFT JOIN LOOKUPS ON words.id = LOOKUPS.word_key WHERE words.lang="en" GROUP BY word;'
    )
    for row in conn.execute(sql):
        word = {
            'text': row[0].strip().lower().encode('utf-8'),
            'context': '',
        }
        if len(row) > 1 and row[1] and isinstance(row[1], unicode):
            word['context'] = row[1].strip().lower().encode('utf-8')
        words.append(word)
    conn.close()
    return words

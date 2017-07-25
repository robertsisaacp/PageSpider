import sqlite3 as lite


def create_database(database_path: str):
    connection = lite.connect(database_path)
    with connection:
        cursor = connection.cursor()
        cursor.execute("drop table if exists words")
        ddl = "CREATE TABLE words(word TEXT PRIMARY KEY NOT NULL, usage_count INT DEFAULT 1 NOT NULL);"
        cursor.execute(ddl)
        ddl = "CREATE UNIQUE INDEX words_word_uindex ON words (word)"
        cursor.execute(ddl)


def save_words_to_database(database_path: str, words_list: list):
    connection = lite.connect(database_path)
    with connection:
        cursor = connection.cursor()
        for word in words_list:
            # check to see if the word is in there
            sql = "select count(word) from words where word='" + word + "'"
            cursor.execute(sql)
            count = cursor.fetchone()[0]
            if count > 0:
                sql = "update words set usage_count = usage_count + 1 where word = '" + word + "'"
            else:
                sql = "insert into words(word) values ('" + word + "')"
            cursor.execute(sql)
    print("database save complete")

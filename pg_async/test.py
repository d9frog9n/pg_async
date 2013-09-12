import argparse
from datetime import datetime

import gevent
from psycogreen.gevent import patch_psycopg
import psycopg2


parser = argparse.ArgumentParser(description='Simple psycogreen sample app')
parser.add_argument(
    'connection_string', type=str,
    help='Database connection string, eg:\n'
         'user:password@127.0.0.1:5432/database')
parser.add_argument(
    '--enable-psycogreen',
    action="store_true",
    help='Enable psycogreen')

if __name__ == '__main__':
    args = parser.parse_args()
    
    if args.enable_psycogreen:
        patch_psycopg()

    connection = psycopg2.connect('postgresql://'+args.connection_string)
    cursor = connection.cursor()

    def loop_log():
        while True:
            print('Log: {}'.format(datetime.now()))
            gevent.sleep(1.0)

    gevent.spawn(loop_log)

    def loop_database():
        while True:
            cursor.execute('select pg_sleep(5);')
            print('Database: OK')
            gevent.sleep(1.0)

    gevent.spawn(loop_database)

    while True:
        try:
            gevent.sleep()
        except KeyboardInterrupt:
            break

    cursor.close()
    connection.close()

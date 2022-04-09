import argparse
from cassandra import InvalidRequest
from cassandra.cluster import Cluster
from cassandra.protocol import SyntaxException


def output(*sequence, newline_before=True, newline_after=True):
    SPACING = 2
    SPACE = " " * (SPACING - 1)
    if newline_before:
        print("")
    if type(sequence[0]) in (tuple, list):
        for line in sequence:
            print(SPACE, *line)
    elif 1 < len(sequence):
        for line in sequence:
            print(SPACE, line)
    else:
        print(SPACE, *sequence)
    if newline_after:
        print("")


parser = argparse.ArgumentParser()
parser.add_argument('ip_addresses', type=str, nargs='*', default="localhost")
parser.add_argument('--port', type=int, default=9042)
args = parser.parse_args()


output(
    ('ip_addresses:', args.ip_addresses),
    ('port:', args.port),
)


output('connecting...', newline_after=False)
cluster = Cluster(args.ip_addresses, port=args.port)
session = cluster.connect()
output('connected!', newline_before=False)


def print_tips():
    output('--- TIPS ---', newline_after=False)
    output(
        "DESCRIBE keyspaces",
        "DESCRIBE tables",
        "USE keyspace_name",
        newline_after=False
    )
    output(
        "CREATE KEYSPACE keyspace_name WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 3}",
        "CREATE KEYSPACE IF NOT EXISTS keyspace_name WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : '3' }",
        "DESCRIBE keyspace_name",
        "DROP KEYSPACE keyspace_name",
        "DROP KEYSPACE IF EXISTS keyspace_name",
        newline_after=False
    )
    output(
        "CREATE TABLE IF keyspace_name.table_name (id text PRIMARY KEY)",
        "CREATE TABLE IF NOT EXISTS keyspace_name.table_name (id text PRIMARY KEY)",
        "DESCRIBE keyspace_name.table_name",
        "DROP TABLE keyspace_name.table_name",
        "DROP TABLE IF EXISTS keyspace_name.table_name"
    )


print_tips()


while True:

    command = input("> ")
    output(command)

    if command == "exit":
        break
    if command == "tips":
        print_tips()
        continue

    try:
        results = session.execute(command)
        for row in results.all():
            output(row, newline_before=False)
    except (SyntaxException, InvalidRequest) as e:
        output(e, newline_before=False)


output('disconnecting...', newline_before=False, newline_after=False)
cluster.shutdown()
output('disconnected, bye!', newline_before=False)

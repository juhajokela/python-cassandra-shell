# Python Cassandra Shell

A lightweight Python app providing an interactive shell for interacting with Apache Cassandra database.

## Run

```
# 0) check that your runtime is compatible (see: runtime.txt)
# 1) install
python3 -m virtualenv venv && source venv/bin/activate && pip install -r requirements.txt
# 2) run
python3 cassandra-shell.py
```

## Demo

```
python3 cassandra-shell.py

  ip_addresses: ['35.228.27.58', '34.88.161.224', '34.88.205.227']
  port: 9042


  connecting...
  connected!


  --- TIPS ---

  CREATE KEYSPACE keyspace_name WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 3}
  CREATE KEYSPACE IF NOT EXISTS keyspace_name WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : '3' }
  DESCRIBE keyspaces
  DROP KEYSPACE keyspace_name
  DROP KEYSPACE IF EXISTS keyspace_name

  CREATE TABLE IF keyspace_name.table_name (id text PRIMARY KEY)
  CREATE TABLE IF NOT EXISTS keyspace_name.table_name (id text PRIMARY KEY)
  DESCRIBE keyspace_name.table_name
  DROP TABLE keyspace_name.table_name
  DROP TABLE IF EXISTS keyspace_name.table_name

> DESCRIBE keyspaces

  DESCRIBE keyspaces

  Row(keyspace_name='system', type='keyspace', name='system')

  Row(keyspace_name='system_auth', type='keyspace', name='system_auth')

  Row(keyspace_name='system_distributed', type='keyspace', name='system_distributed')

  Row(keyspace_name='system_schema', type='keyspace', name='system_schema')

  Row(keyspace_name='system_traces', type='keyspace', name='system_traces')

  Row(keyspace_name='system_views', type='keyspace', name='system_views')

  Row(keyspace_name='system_virtual_schema', type='keyspace', name='system_virtual_schema')

> exit

  exit

  disconnecting...
  disconnected, bye!
```

import Database_manager as db


conn = db.DatabaseManager('postgres', 'password')


conn.connect_to_database('daily_updates')

# conn.list_databases()
# # conn.create_database('daily_updates')

# columns = {
#     'id': 'SERIAL PRIMARY KEY',
#     'title': 'VARCHAR(100) NOT NULL',
#     'description': 'TEXT',
#     'created_at': 'DATE DEFAULT CURRENT_DATE'
# }


# conn.create_table('Daily_update', columns)

update = {
    'title': 'OS Module',
    'description': 'Read and implemented OS module fuction like mkdir, rmdir and many more',
}

# conn.insert_data('daily_update', update)

rawe=conn.show_data('Daily_update')

# # conn.drop_table('daily_updates')
# conn.describe_table('daily_update')


TORTOISE_ORM = {
                'connections': {
                    # Dict format for connection
                    'default': {
                        'engine': 'tortoise.backends.asyncpg',
                        'credentials': {
                            'host': 'localhost',
                            'port': '5432',
                            'user': 'postgres',
                            'password': 'admin',
                            'database': 'test2',
                        }
                    },
                    # Using a DB_URL string
                    'default': 'postgres://postgres:admin@localhost:5432/test2'
                },
                'apps': {
                    'models': {
                        'models': ['main', 'aerich.models'],
                        # If no default_connection specified, defaults to 'default'
                        'default_connection': 'default',
                    }
                }
            }
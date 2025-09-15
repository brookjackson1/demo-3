import os

# Database connection configuration
DB_CONFIG = {
    'host': 'y06qcehxdtkegbeb.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
    'username': 'dvj86e1s5vp5zm84',
    'password': 'mgegvptmo7ahdehu',
    'port': 3306,
    'database': 'cxpc0fj5zjm1j667'
}

# Connection string for SQLAlchemy
DATABASE_URL = f"mysql+pymysql://{DB_CONFIG['username']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"

# Alternative connection string for other MySQL libraries
MYSQL_CONNECTION_STRING = f"mysql://{DB_CONFIG['username']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
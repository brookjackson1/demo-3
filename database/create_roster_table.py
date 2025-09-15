import mysql.connector
from db_config import DB_CONFIG

def create_roster_table():
    try:
        connection = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['username'],
            password=DB_CONFIG['password'],
            database=DB_CONFIG['database'],
            port=DB_CONFIG['port']
        )
        
        cursor = connection.cursor()
        
        create_table_query = """
        CREATE TABLE IF NOT EXISTS georgia_football_roster_2025 (
            id INT AUTO_INCREMENT PRIMARY KEY,
            jersey_number VARCHAR(10),
            full_name VARCHAR(100) NOT NULL,
            position VARCHAR(10),
            height VARCHAR(10),
            weight INT,
            year_class VARCHAR(20),
            hometown VARCHAR(100),
            high_school VARCHAR(100),
            previous_school VARCHAR(100),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        
        cursor.execute(create_table_query)
        connection.commit()
        print("Table 'georgia_football_roster_2025' created successfully!")
        
    except mysql.connector.Error as error:
        print(f"Error creating table: {error}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_roster_table()
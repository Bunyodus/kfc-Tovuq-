import mysql.connector

def create_connection():
    """Create a connection to the MySQL database."""
    conn = mysql.connector.connect(
        host="localhost",
        user="root",         
        password="Bunik_07", 
        database="kfc_orders_db" 
    )
    return conn

def create_table():
    """Create the orders table if it doesn't exist."""
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INT AUTO_INCREMENT PRIMARY KEY,
        item_name VARCHAR(255) NOT NULL,
        quantity INT NOT NULL,
        total_price INT NOT NULL,
        address VARCHAR(255) 
    )
    """)
    conn.commit()
   

def add_order(item_name, quantity, total_price, address):
    """Add a new order to the database."""
    conn = create_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO orders (item_name, quantity, total_price, address)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (item_name, quantity, total_price, address))
    conn.commit()
    conn.close()

def get_orders():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    conn.close()
    return orders


# create_table()
import sqlite3

def setup_mock_database():
    # This simulates our backend database for local testing
    conn = sqlite3.connect('mock_databricks.db')
    cursor = conn.cursor()
    
    # Create the table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS daily_sales_data (
            transaction_date TEXT,
            total_revenue REAL,
            customer_region TEXT,
            transaction_status TEXT
        )
    ''')
    
    # Clear any old data and insert fresh dummy data
    cursor.execute('DELETE FROM daily_sales_data')
    dummy_data = [
        ('2026-06-15', 1500.50, 'North America', 'COMPLETED'),
        ('2026-06-16', 2200.00, 'Europe', 'COMPLETED'),
        ('2026-06-17', 800.75, 'Asia', 'PENDING')
    ]
    cursor.executemany('''
        INSERT INTO daily_sales_data VALUES (?, ?, ?, ?)
    ''', dummy_data)
    
    conn.commit()
    return conn

def run_pipeline():
    conn = setup_mock_database()
    cursor = conn.cursor()
    
    start_date = '2026-06-01'
    end_date = '2026-06-30'
    
    # The pipeline bug is inside this SQL query
    sql_query = f"""
        SELECT 
            transaction_date,
            total_revenu, 
            customer_region
        FROM 
            daily_sales_data
        WHERE 
            transaction_date >= '{start_date}' 
            AND transaction_date <= '{end_date}'
            AND transaction_status = 'COMPLETED';
    """
    
    print("--------------------------------------------------")
    print("Active Batch Trigger Received.")
    print("Sending query to Databricks Cluster (SQLite)...")
    print("--------------------------------------------------\n")
    
    try:
        # Attempt to run the SQL against the database
        cursor.execute(sql_query)
        results = cursor.fetchall()
        
        print("✅ SUCCESS! Pipeline completed. Data retrieved:")
        for row in results:
            print(f"Date: {row[0]} | Revenue: ${row[1]} | Region: {row[2]}")
            
    except sqlite3.OperationalError as error:
        # This will catch the typo and print a realistic error log
        print("❌ [PIPELINE FAILED] Databricks Cluster Error:")
        print(f"Error Details: {error}\n")
        print("Action Required: Please fix the SQL query in the Python script and re-run.")
        
    finally:
        conn.close()

if __name__ == "__main__":
    run_pipeline()
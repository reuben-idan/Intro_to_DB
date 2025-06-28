#!/usr/bin/env python3
"""
MySQL Database Creation Script
Creates the alx_book_store database for the online bookstore project
"""

import mysql.connector

def create_database():
    """
    Creates the alx_book_store database in MySQL server
    """
    connection = None
    try:
        # Connect to MySQL server (without specifying a database)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Add your MySQL password here if needed
            charset="utf8mb4"
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create the database
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")
            
            cursor.close()
            
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        
    finally:
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database() 
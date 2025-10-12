import psycopg2

def get_connection() -> None:
    try:
        connection = psycopg2.connect(
            user="",
            password="",
            host="",
            port="",
            database=""
        )
        cursor = connection.cursor()
        print("Database connection successful")
        return cursor
    
    except (Exception, psycopg2.Error) as error:
        print(f"Error connecting to database: {error}") 
        return None

if __name__ == "__main__":
    pass

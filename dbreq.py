import psycopg2
from config import host, user, password, db_name
from pydantic import BaseModel

data=[]


try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )



    with connection.cursor() as cursor:
        cursor.execute(
            "select * from users"
        )
        data=cursor.fetchall()
    print(data)

    def get_info_for_id(index):
        for tupl in data:
            if tupl[0] == index:
                return tupl





except Exception as _ex:
    print("Error", _ex)
finally:
    if connection:
        connection.close()
        print("Connection close")

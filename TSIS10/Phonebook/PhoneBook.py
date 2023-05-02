# libraries
import psycopg2
from config import configuration

# counting rows of names and phones


def counter_for_name():
    connection = None
    try:
        parametres = configuration()
        connection = psycopg2.connect(**parametres)
        cursor = connection.cursor()
        sql = "SELECT * FROM users;"
        cursor.execute(sql, [])
        current_rows = len(cursor.fetchall())
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return current_rows


def counter_for_phone():
    connection = None
    try:
        parametres = configuration()
        connection = psycopg2.connect(**parametres)
        cursor = connection.cursor()
        sql = "SELECT * FROM phones"
        cursor.execute(sql, [])
        current_rows = len(cursor.fetchall())
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return current_rows


# Creating tables for phones and names


def Create_tables_for_phonebook():
    commands = (
        """
        CREATE TABLE users(
            user_id SERIAL PRIMARY KEY,
            user_name VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE phones(
            phone_id SERIAL PRIMARY KEY,
            user_phone VARCHAR(255) NOT NULL
        )
        """
    )
    connection = None
    try:
        parametres = configuration()
        connection = psycopg2.connect(**parametres)
        cursor = connection.cursor()
        for command in commands:
            cursor.execute(command)
        cursor.close()
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

# inserting one name


def insert_name(user_name):
    data = """INSERT INTO users(user_name)
              VALUES(%s) RETURNING user_id;"""
    connection = None
    try:
        parametres = configuration()
        connection = psycopg2.connect(**parametres)
        cursor = connection.cursor()
        cursor.execute(data, (user_name,))
        user_id = cursor.fetchone()[0]
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return user_id

# inserting one phone


def insert_phone(name_of_phone):
    data = """INSERT INTO phones(user_phone) 
    VALUES (%s) RETURNING phone_id"""
    connection = None
    try:
        parametres = configuration()
        connection = psycopg2.connect(**parametres)
        cursor = connection.cursor()
        cursor.execute(data, (name_of_phone,))
        phone_id = cursor.fetchone()[0]
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return phone_id

# updating user name


def updating_user_name(user_id, user_name):
    data = """UPDATE users
                SET user_name=%s
                WHERE user_id=%s
    """
    connection = None
    try:
        parametres = configuration()
        connection = psycopg2.connect(**parametres)
        cursor = connection.cursor()
        cursor.execute(data, (user_name, user_id,))
        cursor.close()
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

# updating user phone


def updating_user_phone(phone_id, user_phone):
    data = """UPDATE phones
                SET user_phone=%s
                WHERE phone_id=%s
    """
    connection = None
    try:
        parametres = configuration()
        connection = psycopg2.connect(**parametres)
        cursor = connection.cursor()
        cursor.execute(data, (user_phone, phone_id))
        cursor.close()
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


# getting table of phones
def getting_user_phone():
    connection = None
    try:
        parametres = configuration()
        connection = psycopg2.connect(**parametres)
        cursor = connection.cursor()
        cursor.execute(
            """SELECT phone_id,user_phone FROM phones ORDER BY phone_id""")
        print(f"Total number of phones:{cursor.rowcount}")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


# getting table of names
def getting_user_name():
    connection = None
    try:
        parametres = configuration()
        connection = psycopg2.connect(**parametres)
        cursor = connection.cursor()
        cursor.execute(
            """SELECT user_id, user_name FROM users ORDER BY user_id""")
        print(f"Total number of names:{cursor.rowcount}")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


# deleting name and phone by id
def deleting(user_id):
    connection = None
    try:
        parametres = configuration()
        connection = psycopg2.connect(**parametres)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
        cursor.execute("DELETE FROM phones WHERE phone_id = %s", (user_id,))
        cursor.close()
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


# main function
rows_of_name = counter_for_name()
rows_of_phone = counter_for_phone()
if __name__ == "__main__":
    print("""
Choose one of this options:
1.Inserting user name                   2.Inserting  user phone
3.Updating user name                    4.Updating user phone
5.Getting user name                     6.Getting user phone
7.Deleting user name and phone          8.Stop program
(BE CAREFUL the amount of user phone can't be greater than user name)
Please enter the number:""", end="")
    number = int(input())
    exit = True
    while (exit):
        if (number == 1):
            print("Insert name:", end="")
            name = input()
            rows_of_name = counter_for_name()+1
            insert_name(name)
            number = 0
        elif (number == 2):
            print("Insert phone:", end="")
            phone = input()
            rows_of_phone = counter_for_phone()+1
            if (rows_of_phone > rows_of_name):
                print(
                    "Number of phones greater than number of names, unfortunatelly you can not insert this phone")
            else:
                insert_phone(phone)
            number = 0
        elif (number == 3):
            print("Enter the name of user:", end="")
            user_name = input()
            print("Enter the ID of user:", end="")
            user_id = int(input())
            updating_user_name(user_id, user_name)
            number = 0
        elif (number == 4):
            print("Enter the phone of user:", end="")
            user_phone = input()
            print("Enter the ID of user:", end="")
            phone_id = int(input())
            updating_user_phone(phone_id, user_phone)
            number = 0
        elif (number == 5):
            getting_user_name()
            number = 0
        elif (number == 6):
            getting_user_phone()
            number = 0
        elif (number == 7):
            print("Enter ID which will be deleted:", end="")
            deleted_id = int(input())
            deleting(deleted_id)
            number = 0
        elif (number == 8):
            break
        else:
            print("Please enter the number between 1-8(included):")
            number = int(input())

        if (number == 0):
            print("""
Choose one of this options:
1.Inserting user name                   2.Inserting user phone
3.Updating user name                    4.Updating user phone
5.Getting user name                     6.Getting user phone
7.Deleting user name and phone          8.Stop program
(BE CAREFUL the amount of user phone can't be greater than user name)
Please enter the number:
""", end="")
            number = int(input())
print("THANKS FOR USING THIS PROGRAM")

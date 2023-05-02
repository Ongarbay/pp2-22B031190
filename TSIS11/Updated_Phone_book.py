# libraries
import psycopg2
import re
import pygame
from config import configuration
pygame.init()

# creating table


def creating_table():
    command = (
        """
        CREATE TABLE IF NOT EXISTS users(
            user_id SERIAL PRIMARY KEY,
            user_name VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS phones(
            phone_id SERIAL PRIMARY KEY,
            user_phone VARCHAR(11) NOT NULL
        )
        """
    )
    connection = None
    try:
        parametres = configuration()
        connection = psycopg2.connect(**parametres)
        cursor = connection.cursor()
        for row in command:
            cursor.execute(row)
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

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

# inserting new user


def inserting_new_user(new_name, new_phone):
    connection = None
    sql = """SELECT user_name,user_id FROM users ORDER BY user_id"""
    try:
        parametres = configuration()
        connection = psycopg2.connect(**parametres)
        list_of_names = []
        check = False
        id_of_name = 0
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            list_of_names.append(row)
        for name in range(len(list_of_names)):
            if list_of_names[name][0] == new_name:
                id_of_name = list_of_names[name][1]
                sql = """UPDATE phones
                            SET user_phone=%s
                            WHERE phone_id=%s
                """
                check = True
        if check:
            cursor.execute(sql, (new_phone, id_of_name))
        else:
            sql1 = """INSERT INTO phones(user_phone) VALUES(%s) RETURNING phone_id"""
            sql2 = """INSERT INTO users(user_name)  VALUES(%s) RETURNING user_id"""
            cursor.execute(sql1, (new_phone,))
            cursor.execute(sql2, (new_name,))
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

# Inserting list of users


def inserting_list_of_users(list_of_data):
    connection = None
    list_of_names = list_of_data[0]
    list_of_phones = list_of_data[1]
    sql_insert1 = """INSERT INTO phones(user_phone) VALUES(%s) RETURNING phone_id"""
    sql_insert2 = """INSERT INTO users(user_name) VALUES(%s) RETURNING user_id"""
    sql_check = """SELECT user_name, user_id FROM users ORDER BY user_id;"""
    sql_update = """UPDATE phones
                    SET user_phone=%s
                    WHERE phone_id=%s"""

    try:
        parametres = configuration()
        connection = psycopg2.connect(**parametres)
        cursor = connection.cursor()
        cursor.execute(sql_check)
        current_names = cursor.fetchall()

        for i in range(len(current_names)):
            check = False
            for j in range(len(list_of_names)):
                if current_names[i][0] == list_of_names[j]:
                    cursor.execute(
                        sql_update, (list_of_phones[j], current_names[i][1],))
                    check = True
                    break
            if not check:
                cursor.execute(sql_insert1, (list_of_phones[j],))
                cursor.execute(sql_insert2, (list_of_names[j],))
        cursor.close()
        connection.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

# Getting data from table


def getting_data_from_table(option):
    connection = None

    # Only names
    sql1 = """SELECT user_id, user_name FROM users ORDER BY user_id 
        """
    # Only phones
    sql2 = """SELECT phone_id, user_phone FROM phones ORDER BY phone_id
        """
    # All together
    sql3 = """SELECT phone_id, user_phone FROM phones ORDER BY phone_id"""
    sql4 = """SELECT user_id, user_name FROM users ORDER BY user_id"""
    try:
        parametres = configuration()
        connection = psycopg2.connect(**parametres)
        cursor = connection.cursor()
        if (option == 1):
            cursor.execute(sql1)
            rows = cursor.fetchall()
            print(f"Total number of rows:{len(rows)}")
            for i in rows:
                print("User ID:{0:<5}  | Name:{1:<20}".format(i[0], i[1]))
        if (option == 2):
            cursor.execute(sql2)
            rows = cursor.fetchall()
            print(f"Total number of rows:{len(rows)}")
            for i in rows:
                print("User ID:{0:<5}  | Phone:{1:<20}".format(i[0], i[1]))
        if (option == 3):
            cursor.execute(sql3)
            phones = cursor.fetchall()
            cursor.execute(sql4)
            names = cursor.fetchall()
            print(f"Total number of rows:{len(names)}")
            for i in range(len(names)):
                print("User ID:{0:<5}  | Name:{1:<20}  | Phone:{2}".format(
                    names[i][0], names[i][1], phones[i][1]))
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
# Deleting by phone or name


def deleting_user(option, data):
    connection = None
    user_id = 0
    sql = """"""
    if option == 1:
        sql = """SELECT user_name,user_id FROM users ORDER BY user_id"""
    if option == 2:
        sql = """SELECT user_phone,phone_id FROM phones ORDER BY phone_id"""
    try:
        parametres = configuration()
        connection = psycopg2.connect(**parametres)
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for i in rows:
            if i[0] == data:
                user_id = i[1]
        if user_id == 0:
            if option == 1:
                print("There is no such name!")
            if option == 2:
                print("There is no such phone!")
        else:
            cursor.execute("DELETE FROM users WHERE user_id=%s", (user_id,))
            cursor.execute("DELETE FROM phones WHERE phone_id=%s", (user_id,))
            cursor.close()
            connection.commit()
            print("Deleting was succesfully!")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

# Pagination users


def pagination_of_table():
    connection = None
    sql1 = """SELECT user_id,user_name FROM users ORDER BY user_id"""
    sql2 = """SELECT phone_id,user_phone FROM phones ORDER BY phone_id"""

    try:
        parametres = configuration()
        connection = psycopg2.connect(**parametres)
        list_of_users = []
        cursor = connection.cursor()
        cursor.execute(sql1)
        rows_of_name = cursor.fetchall()
        cursor.execute(sql2)
        rows_of_phone = cursor.fetchall()

        for i in range(len(rows_of_name)):
            element = []
            element.append(rows_of_name[i][0]), element.append(
                rows_of_name[i][1]), element.append(rows_of_phone[i][1])
            list_of_users.append(element)

        index = 0
        condition = True
        print(f"Number of users is:{len(list_of_users)}")
        print("Click 'n' or 'N' to next user, Click 's' or 'S' to stop pagination")
        print("User ID:{0:<5}  | Name:{1:<20}  | Phone:{2}".format(
            list_of_users[0][0], list_of_users[0][1], list_of_users[0][2]))
        check = False
        key = ""
        while condition:
            if not check:
                key = input()
                if key == 'n' or 'N':
                    index += 1
                    check = True
                elif key == 's' or 'S':
                    condition = False
            if index == len(list_of_users):
                print("You checked all users!")
                break
            else:
                print("User ID:{0:<5}  | Name:{1:<20}  | Phone:{2}".format(
                    list_of_users[index][0], list_of_users[index][1], list_of_users[index][2]))
                check = False

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
# main function


exit = True
print("""Please choose one of this options:
1.Inserting list of users(Checking)           2.Querying data(Pagination)
3.Getting table(by pattern)                   4.Inserting user(if name exists, update phone)
5.Deleting user(by name or phone)             6.Stop program
Please enter the number:""", end="")
number = int(input())

if __name__ == "__main__":
    creating_table()
    while exit:
        if number == 1:
            list_of_data = []
            list_of_names = []
            list_of_phones = []
            list_of_incorrect_phones = []

            size = int(input("Please enter the number of new users:"))
            for i in range(size):
                new_name = input(f"Please enter the {i+1} name:")
                new_phone = input(f"Please enter the {i+1} phone:")
                check = re.match("^[0-9]{11}", new_phone)
                if check and len(new_name) > 0:
                    list_of_names.append(new_name)
                    list_of_phones.append(new_phone)
                else:
                    list_of_incorrect_phones.append(new_phone)

            number = 0
            list_of_data.append(list_of_names)
            list_of_data.append(list_of_phones)
            inserting_list_of_users(list_of_data)
            print(f"Your incorrect phones:{list_of_incorrect_phones}")

        elif number == 2:
            pagination_of_table()
            number = 0

        elif number == 3:
            print(
                "Choose the pattern of sorting:   1.Only names   2.Only phones   3.Full table")
            option = int(input())
            getting_data_from_table(option)
            number = 0

        elif number == 4:
            new_name = input("Please enter the name:")
            new_phone = input("Please enter the phone:")
            check = re.search("^[0-9]{11}", new_phone)
            if check and len(new_name) != 0:
                inserting_new_user(new_name, new_phone)
            else:
                print(
                    f"Your phone:{new_phone}  Phone must include 11 digits!(Insert doesn't completed)")
            number = 0

        elif number == 5:
            print("Choose the pattern of deleting:", end="")
            option = int(
                input(f"  1.Deleting by name     2.Deleting by phone      Your Number:"))
            data = ""
            if option == 1:
                data = input("Enter the name of user:")
            if option == 2:
                data = input("Enter the phone of user:")
            deleting_user(option, data)
            number = 0

        elif number == 6:
            print("Thanks for using this program!")
            exit = False

        else:
            print("Please enter the number between 1-6(included):", end="")
            number = int(input())

        if (number == 0):
            print("""Please choose one of this options:
1.Inserting list of users(Checking)           2.Querying data(Pagination)
3.Getting table(by pattern)                   4.Inserting user(if name exists, update phone)
5.Deleting user(by name or phone)             6.Stop program
Please enter the number:""", end="")
            number = int(input())

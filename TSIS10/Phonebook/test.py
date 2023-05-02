import psycopg2
from config import configuration


def insert_vendor(vendor_name):
    sql = """
    INSERT INTO vendors(vendor_name)
    VALUES(%s) RETURNING vendor_id"""
    conn = None
    vendor_id = None
    try:
        # read the connection parameters
        params = configuration()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (vendor_name,))
        vendor_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return vendor_id


def insert_vendor_list(vendor_list):
    conn = None
    sql = "INSERT INTO vendors(vendor_name) VALUES(%s)"
    try:
        params = configuration()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.executemany(sql, vendor_list)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def update_vendor(vendor_id, vendor_name):
    sql = """UPDATE vendors
            SET vendor_name=%s
            WHERE vendor_id=%s 
    """
    conn = None
    try:
        params = configuration()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.execute(sql, (vendor_name, vendor_id))
        updated_rows = cursor.rowcount
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return updated_rows


def add_part(part_name, vendor_list):
    insert_part = "INSERT INTO parts(part_name) VALUES(%s) RETURNING part_id"
    assign_vendor = "INSERT INTO vendor_parts(vendor_id,part_id) VALUES (%s,%s)"
    conn = None
    try:
        params = configuration()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.execute(insert_part, (part_name,))
        part_id = cursor.fetchone()[0]
        for vendor_id in vendor_list:
            cursor.execute(assign_vendor, (vendor_id, part_id))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def get_vendors():
    conn = None
    try:
        params = configuration()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT vendor_id,vendor_name FROM vendors ORDER BY vendor_name")
        print("The number of parts:", cursor.rowcount)
        row = cursor.fetchone()
        while row is not None:
            print(row)
            row = cursor.fetchone()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def delete_part(part_id):
    conn = None
    rows_deleted = 0
    try:
        params = configuration()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM parts WHERE part_id =%s", (part_id,))
        rows_deleted = cursor.rowcount
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return rows_deleted


if __name__ == "__main__":
    get_vendors()

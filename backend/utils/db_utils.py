# utils/db_utils.py
import aiomysql

async def get_db_connection():
    return await aiomysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='password',
        db='trinity',
        autocommit=True
    )

async def execute_query(query, args=None):
    conn = await get_db_connection()
    try:
        cur = await conn.cursor()
        await cur.execute(query, args)
        await conn.commit()
        return await cur.fetchall()
    finally:
        conn.close()

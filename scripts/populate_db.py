import asyncio
import os
import random as ra
import sys
from datetime import datetime

import psycopg

"""
sys.argv[1] -> number of records to be populated
"""

user_name = "p_user"
user_password = "p_password"
db_host = "0.0.0.0"
db_port = 5432


async def commit_transactions(number_of_records):
    async with await psycopg.AsyncConnection.connect(
        f"host={db_host} port={db_port} user={user_name} password={user_password}"
    ) as conn:
        async with conn.cursor() as cur:
            for i in range(number_of_records):
                await cur.execute(
                    "INSERT INTO raw_data (creation_time, value) VALUES (%s, %s)",
                    (datetime.now(), random_number()),
                )
            await conn.commit()


def random_number(lower_range=0, upper_range=10**6):
    return ra.randint(lower_range, upper_range)


async def populate_db(records):
    await commit_transactions(records)


if __name__ == "__main__":
    asyncio.run(populate_db(int(sys.argv[1])))

"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

import asyncio
from dataclasses import dataclass

from aiohttp import ClientSession
from loguru import logger


@dataclass
class Service:
    name: str
    url: str
    field: str


SERVICES = [
    Service("users", USERS_DATA_URL, ""),
    Service("posts", POSTS_DATA_URL, ""),
]

async def fetch_json(session: ClientSession, url: str) -> list:
    async with session.get(url) as response:
        return await response.json()


async def fetch_users(service) -> str:
    logger.info("Fetch users from {}", service.name)

    async with ClientSession() as session:
        result = await fetch_json(session, service.url)

    logger.info("Fetched json from {!r}: {}", service.name, result)

    return result


async def fetch_posts(service) -> str:
    logger.info("Fetch posts from {}", service.name)

    async with ClientSession() as session:
        result = await fetch_json(session, service.url)

    logger.info("Fetched json from {!r}: {}", service.name, result)

    return result

def main():
    logger.info("Starting main")
    users = asyncio.run(fetch_users(SERVICES[0]))
    logger.info("Finishing main")




if __name__ == '__main__':
    main()
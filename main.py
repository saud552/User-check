import asyncio

nest_asyncio.apply()

from add import main
from User_check import main

if __name__ == "__main__":
    asyncio.run(main())

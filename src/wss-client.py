#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# created_on: 2018-11-12 17:24

"""
wss-client.py
"""


import asyncio
import pathlib
import ssl
import websockets


__author__ = "Toran Sahu <toran.sahu@yahoo.com>"
__license__ = "Distributed under terms of the MIT license"


ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ssl_context.load_verify_locations(pathlib.Path(__file__).with_name("ca-certificates.crt"))


async def push():
    """Push data to websocket server securely"""
    async with websockets.connect(
        "wss://echo.websocket.org", ssl=ssl_context
    ) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")


asyncio.get_event_loop().run_until_complete(push())

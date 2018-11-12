#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# created_on: 2018-11-12 17:07

"""
ws-client.py
"""


import asyncio
import websockets


__author__ = "Toran Sahu <toran.sahu@yahoo.com>"
__license__ = "Distributed under terms of the MIT license"


async def push():
    """Push message to websocket server"""
    async with websockets.connect("ws://echo.websocket.org") as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(push())

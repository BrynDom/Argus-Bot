# Copyright (C) 2022-2023 
#
# This file is a part of < https://github.com/AyiinXd/Ayiin-Userbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/Ayiin-Userbot/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>

import asyncio

from pyrogram import *

from Mix import *


@ky.ubot("argus", sudo=True)
async def _(c: nlx, m):
    uputt = await m.reply("**Hai... Perkenalkan Saya Adalah Argus-Userbot**")
    asyncio.sleep(3)
    await uputt.edit("**Userbot base on Pyrogram**")
    asyncio.sleep(2)
    await uputt.edit("**Part Of @TeamAllBots... Salam Kenal yaaa ><**")
    asyncio.sleep(3)
    await uputt.edit(
        "**Repository [Argus-Userbot](https://github.com/BrynDom/Argus-Bot)**"
    )


# Create by myself


@ky.ubot("sayang", sudo=True)
async def _(c: nlx, m):
    xx = await m.reply("**Aku Cuma Mau Bilang...**", reply_to_message_id=ReplyCheck(m))
    asyncio.sleep(3)
    await xx.edit("**Aku Sayang Kamu Mwaahh** 😘❤")


# Create by myself


@ky.ubot("semangat", sudo=True)
async def _(c: nlx, m):
    uputt = await m.reply(
        "**Apapun Yang Terjadi...**", reply_to_message_id=ReplyCheck(m)
    )
    await asyncio.sleep(1.8)
    await uputt.edit("**Tetaplah Bernafas...**")
    await asyncio.sleep(1.8)
    await uputt.edit("**Dan Bersyukur...**")


# Create by myself


@ky.ubot("mengeluh", sudo=True)
async def _(c: nlx, m):
    uputt = await m.reply(
        "**Apapun Yang Terjadi...**", reply_to_message_id=ReplyCheck(m)
    )
    await asyncio.sleep(1.8)
    await uputt.edit("**Tetaplah Mengeluh...**")
    await asyncio.sleep(1.8)
    await uputt.edit("**Dan Putus Asa...**")


# Create by myself

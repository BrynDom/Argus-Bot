################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || Misskaty
  • JANGAN DIHAPUS YA MONYET-MONYET SIALAN
 
 MIKIR GOBLOK, TOLOL, IDIOT, NGENTOT, KONTOL, BAJINGAN
"""
################################################################

import os
import random
from io import BytesIO

from pyrogram.types import *

from Mix import *
from Mix.core.tools_quote import *

__modles__ = "Quote"
__help__ = get_cgr("help_qot")


@ky.ubot("q", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    acak = None
    messages = []
    rep = m.reply_to_message

    # Memeriksa apakah ada pesan yang di-reply dan pesan tersebut berisi teks atau media yang dapat diproses
    if rep:
        if rep.text or rep.media:
            if len(m.command) < 2:
                acak = random.choice(loanjing)
            else:
                tag = m.command[1].strip()
                c.get_arg(m)

                if tag.startswith("@"):
                    user_id = tag[1:]
                    try:
                        org = await c.get_users(user_id)
                        if org.id in DEVS:
                            await m.reply(cgr("qot_3").format(em.gagal))
                            return
                        rep = await c.get_messages(
                            m.chat.id, m.reply_to_message.id, replies=0
                        )
                        rep.from_user = org
                        messages = [rep]
                    except Exception as e:
                        return await m.reply(cgr("err").format(em.gagal, e))
                    warna = m.text.split(None, 2)[2] if len(m.command) > 2 else None
                    if warna:
                        acak = warna
                    else:
                        acak = random.choice(loanjing)
                elif not tag.startswith("@"):
                    warna = m.text.split(None, 1)[1] if len(m.command) > 1 else None
                    if warna:
                        acak = warna
                    else:
                        acak = random.choice(loanjing)
                    m_one = await c.get_messages(
                        chat_id=m.chat.id, message_ids=m.reply_to_message.id, replies=0
                    )
                    messages = [m_one]
        else:
            return await m.reply(
                "Balasan tidak dapat diproses karena tidak ada teks atau media yang ditemukan."
            )
    else:
        if len(m.command) < 2:
            # Jika tidak ada pesan yang dibalas dan tidak ada argumen username, gunakan id pengirim pesan sebagai pengganti id pengguna yang ditargetkan
            user_id = m.from_user.id
            try:
                org = await c.get_users(user_id)
                if org.id in DEVS:
                    await m.reply(cgr("qot_3").format(em.gagal))
                    return
                messages = [m]
            except Exception as e:
                return await m.reply(cgr("err").format(em.gagal, e))
            warna = m.text.split(None, 1)[1] if len(m.command) > 1 else None
            if warna:
                acak = warna
            else:
                acak = random.choice(loanjing)
        else:
            return await m.reply(
                "Tidak ada pesan yang di-reply dan tidak ada argumen username yang diberikan."
            )

    try:
        hasil = await quotly(messages, acak)
        bs = BytesIO(hasil)
        bs.name = "mix.webp"
        await m.reply_sticker(bs)
    except Exception as e:
        return await m.reply(cgr("err").format(em.gagal, e))


@ky.ubot("qcolor", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    iymek = f"\n• ".join(loanjing)
    jadi = cgr("qot_1").format(em.proses)
    if len(iymek) > 4096:
        with open("qcolor.txt", "w") as file:
            file.write(iymek)
        await m.reply_document("qcolor.txt", caption=cgr("qot_2").format(em.sukses))
        os.remove("qcolor.txt")
    else:
        await m.reply(jadi + iymek)


"""
@ky.ubot("q", sudo=True)
async def _(c: user, m):
    em = Emojik()
    em.initialize()
    acak = None
    messages = None
    tag = m.command[1].strip()
    c.get_arg(m)
    if len(m.command) > 1:
        if tag.startswith("@"):
            user_id = tag[1:]
            try:
                org = await c.get_users(user_id)
                if org.id in DEVS:
                    await m.reply(cgr("qot_3").format(em.gagal))
                    return
                rep = await c.get_messages(m.chat.id, m.reply_to_message.id, replies=0)
                rep.from_user = org
                messages = [rep]
            except Exception as e:
                return await m.reply(cgr("err").format(em.gagal, e))
            warna = m.text.split(None, 2)[2] if len(m.command) > 2 else None
            if warna:
                acak = warna
            else:
                acak = random.choice(loanjing)
        elif not tag.startswith("@"):
            warna = m.text.split(None, 1)[1] if len(m.command) > 1 else None
            if warna:
                acak = warna
            else:
                acak = random.choice(loanjing)
            m_one = await c.get_messages(
                chat_id=m.chat.id, message_ids=m.reply_to_message.id, replies=0
            )
            messages = [m_one]
    else:
        if tag.isnumeric():
            if int(tag) > 10:
                return await m.reply(cgr("qot_4").format(em.gagal))
            warna = m.text.split(None, 2)[2] if len(m.command) > 2 else None
            if warna:
                acak = warna
            else:
                acak = random.choice(loanjing)
            messages = [
                i
                for i in await c.get_messages(
                    chat_id=m.chat.id,
                    message_ids=range(
                        m.reply_to_message.id,
                        m.reply_to_message.id + int(tag),
                    ),
                    replies=0,
                )
                if not i.empty and not i.media
            ]
        else:
            m_one = await c.get_messages(
                chat_id=m.chat.id, message_ids=m.reply_to_message.id, replies=0
            )
            messages = [m_one]
    try:
        hasil = await quotly(messages, acak)
        bs = BytesIO(hasil)
        bs.name = "mix.webp"
        await m.reply_sticker(bs)
    except Exception as e:
        return await m.reply(cgr("err").format(em.gagal, e))
"""

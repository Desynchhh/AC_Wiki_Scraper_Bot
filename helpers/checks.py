import discord

import json

def is_bot_owner(ctx):
    return ctx.author.id == 228179496807694336

def is_owner(ctx):
    return ctx.author.id is ctx.guild.owner.id

def is_admin(ctx):
    if is_bot_owner(ctx) or is_owner(ctx):
        return True
    return ctx.author.id in get_admins()


def get_admins():
    with open('adminlist.json') as f:
        adminlist = json.load(f)
    return adminlist['admins']
import argparse
import discord
import json

from roll import parseRollArgs

with open('creds.json', 'r') as credfile:
    creds = json.load(credfile)

client = discord.Client()

parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(help="sub-command help")

parser_roll = subparsers.add_parser("roll", help="roll help")
roll_group = parser_roll.add_mutually_exclusive_group()
roll_group.add_argument("-a", "--advantage", action="store_true")
roll_group.add_argument("-d", "--disadvantage", action="store_true")
roll_group.add_argument("-v", "--verbose", action="store_true")
parser_roll.add_argument(
    "dice", help="dice to roll, format XdY, which would roll a Y-sided dice X times", action="extend", nargs="+", type=str)

# parser_init = subparsers.add_parser("init", help="init help")
# init_group = parser_roll.add

# args = parser.parse_args()
# parseRollArgs(args.dice, args.advantage, args.disadvantage)


@client.event
async def on_ready():
    for guildname in creds["GUILDS"]:
        guild = discord.utils.get(client.guilds, name=guildname)

        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )


@client.event
async def on_message(message):
    # message.author
    # message.content
    # message.channel.send(response)
    if message.author == client.user:
        return

    cleanmsg = message.content.lower().strip()

    toks = cleanmsg.split(" ")
    if (toks[0] == "roll"):
        args = parser.parse_args(toks)
        if args.dice:
            resp = parseRollArgs(
                args.dice, args.advantage, args.disadvantage)
            await message.channel.send(resp)

client.run(creds["TOKEN"])

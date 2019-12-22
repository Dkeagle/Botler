# Bot Main File
# Dylan "Dkeagle" TAILDEMAN

# Loading modules
import discord
from discord.ext import commands
from log import log_time

# Copying config file into constants
from config import admin_id_list, bot_prefix, bot_token
ADMIN_ID = admin_id_list
PREFIX = bot_prefix
TOKEN = bot_token

# Variables
bot = commands.Bot(command_prefix=PREFIX)

# Disable the default help command
bot.remove_command("help")

# EVENTS
# When the bot is ready
@bot.event
async def on_ready():
	print("{}: Mog logged in!".format(log_time()))

# On every message, if it is a command, convert it to lowercase and print it in the log
@bot.event
async def on_message(message):
	if message.content.startswith(PREFIX):
		message.content = message.content.lower()
		print("{}: {} ({}) in #{}: {}".format(log_time(), message.author.name, message.author.nick, message.channel.name, message.content))
	await bot.process_commands(message)

# If there's an error in the command (or if it's an unknown one)
@bot.event
async def on_command_error(ctx, error):
	split = ctx.message.content.split()
	await ctx.send("La commande \"{}\" n'existe pas, Kupo!".format(split[0]))

# When the bot is disconnected
@bot.event
async def on_disconnect():
	print("{}: Mog logging out!".format(log_time()))

# COMMANDS
# Turn off the bot
@bot.command()
async def stop(ctx):
	if int(ctx.author.id) in ADMIN_ID:
		await ctx.send("Kupo!")
		await bot.logout()
	else:
		await ctx.send("Non, je reste!")

if __name__ == "__main__":
	# Load extensions
	bot.load_extension("help")
	bot.load_extension("dice")

	# Start the bot
	bot.run(TOKEN)
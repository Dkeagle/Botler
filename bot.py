# Bot Main File
# Dylan "Dkeagle" TAILDEMAN

# Loading modules
import discord
from discord.ext import commands
from log import log_time

# Loading config file into constants
from config import admin_id_list, bot_name, bot_prefix, bot_token
ADMIN_ID = admin_id_list
NAME = bot_name
PREFIX = bot_prefix
TOKEN = bot_token

# Create the bot object
bot = commands.Bot(command_prefix=PREFIX)

# Disable the default help command
bot.remove_command("help")

# EVENTS
# When the bot is ready
@bot.event
async def on_ready():
	print("{}: {} logged in!".format(log_time(), NAME))

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
	await ctx.send("La commande \"{}\" n'existe pas!".format(split[0]))

# When the bot is disconnected
@bot.event
async def on_disconnect():
	print("{}: {} logging out!".format(log_time(), NAME))

# COMMANDS
# Turn off the bot
@bot.command()
async def logout(ctx):
	if int(ctx.author.id) in ADMIN_ID:
		await ctx.send("Au revoir!")
		await bot.logout()
	else:
		await ctx.send("Vous n'êtes pas autorisé à exécuter cette commande!")

if __name__ == "__main__":
	# Load extensions
	bot.load_extension("help")
	bot.load_extension("dice")
	
	# Start the bot
	bot.run(TOKEN)
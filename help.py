# Loading modules
from discord.ext import commands

# Commands
@commands.command()
async def help(ctx):
	await ctx.send("Hello World!")

# Adding the commands to the bot
def setup(bot):
	try:
		bot.add_command(help)
	except:
		print("Error: Help not loaded!")
	else:
		print("Help loaded")

if __name__ == "__main__":
	print("This module is part of the MogBot project and should not be used alone. Try starting bot.py")
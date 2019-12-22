# Loading modules
from discord.ext import commands
from random import randint

# Functions
def dice(max):
	return "{}.".format(randint(1, max))

# Commands
@commands.command()
async def d4(ctx):
	await ctx.send(dice(4))

@commands.command()
async def d6(ctx):
	await ctx.send(dice(6))

@commands.command()
async def d8(ctx):
	await ctx.send(dice(8))
	
@commands.command()
async def d10(ctx):
	await ctx.send(dice(10))
	
@commands.command()
async def d12(ctx):
	await ctx.send(dice(12))
	
@commands.command()
async def d20(ctx):
	await ctx.send(dice(20))
	
@commands.command()
async def d100(ctx):
	await ctx.send(dice(100))

# Adding the commands to the bot
def setup(bot):
	try:
		bot.add_command(d4)
		bot.add_command(d6)
		bot.add_command(d8)
		bot.add_command(d10)
		bot.add_command(d12)
		bot.add_command(d20)
		bot.add_command(d100)
	except:
		print("Error: Dice not loaded!")
	else:
		print("Dice loaded")

if __name__ == "__main__":
	print("This module is part of the MogBot project and should not be used alone. Try starting bot.py")
import discord 
from discord.ext import commands
from discord.ext.commands import has_permissions

bot = commands.Bot(command_prefix='.')

@bot.command()
@has_permissions(administrator=True)
async def kickMembers(ctx, role: discord.Role, reason: str = None):
    await ctx.reply('Kicking members')

    for member in role.members:
        await member.kick(reason=reason)

    await ctx.reply('Members kicked')
    

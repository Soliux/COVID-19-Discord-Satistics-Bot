import discord, requests, json, os
from discord.ext import commands

# Feel free to change the bot prefix.
prefix = "."
bot = commands.Bot(command_prefix = prefix)
bot.remove_command("help")
# Change this to the token of the bot you want to run this with.
token = "BOT TOKEN HERE"

@bot.event
async def on_ready():
    print("COVID-19 Bot is now online!")
    await bot.change_presence(activity = discord.Game(name = f"{prefix}help for the usage of the bot"))

@bot.command()
async def world(ctx):
    embed = discord.Embed(
        title = "COVID-19 Global Satistics",
        colour = ctx.author.colour
    )
    api = requests.get("https://covid19.mathdro.id/api").json()
    confirmedCases = api["confirmed"]["value"]
    recoveredCases = api["recovered"]["value"]
    deaths = api["deaths"]["value"]
    embed.add_field(name = "Infected People", value = confirmedCases)
    embed.add_field(name = "People Recovered", value = recoveredCases)
    embed.add_field(name = "Deaths", value = deaths)
    embed.set_image(url = "https://covid19.mathdro.id/api/og")
    await ctx.send(embed = embed)

@bot.command()
async def country(ctx, country):
    embed = discord.Embed(
        title = f"COVID-19 Satistics for {country}",
        colour = ctx.author.colour
    )
    api = requests.get(f"https://covid19.mathdro.id/api/countries/{country}").json()
    confirmedCases = api["confirmed"]["value"]
    recoveredCases = api["recovered"]["value"]
    deaths = api["deaths"]["value"]
    embed.add_field(name = "Infected People", value = confirmedCases)
    embed.add_field(name = "People Recovered", value = recoveredCases)
    embed.add_field(name = "Deaths", value = deaths)
    embed.set_image(url = f"https://covid19.mathdro.id/api/countries/{country}/og")
    await ctx.send(embed = embed)

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title = "COVID-19 Help Command",
        colour = ctx.author.colour,
        description = """
        **So you need some help?**
        **__Commands__**
        **.world** - This will return the global cases.

        **.country <country>** - This will return the COVID-19 cases for the specified country
        Command Example: .country US

        To input a country it must be the abbreviation [here](https://sustainablesources.com/resources/country-abbreviations/) is a list of all country abbreviations.
        """
    )
    await ctx.send(embed = embed)



bot.run(token)
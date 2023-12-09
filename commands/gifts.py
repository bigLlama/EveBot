import discord
from discord.ext import commands
from discord.ext.commands import CommandError
from discord import app_commands
import sqlite3


def update_database(user_id, server_id, sent_gifts, received_gifts):
    # Connect to the SQLite database
    db = sqlite3.connect('eve.sqlite')
    cursor = db.cursor()

    # Check if the record exists
    cursor.execute(f"SELECT * FROM gifts WHERE user_id = ? AND server_id = ?", (user_id, server_id))
    result = cursor.fetchone()

    if result:
        cursor.execute("""
            UPDATE gifts
            SET gifts_sent = gifts_sent + ?,
                gifts_received = gifts_received + ?
            WHERE user_id = ? AND server_id = ?
        """, (sent_gifts, received_gifts, user_id, server_id))
    else:
        cursor.execute("""
            INSERT INTO gifts(user_id, server_id, gifts_sent, gifts_received)
            VALUES(?, ?, ?, ?)
        """, (user_id, server_id, sent_gifts, received_gifts))

    db.commit()
    cursor.close()
    db.close()


class Gifts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='gift', description="Send a gift to a player!")
    @app_commands.checks.cooldown(1, 3600.0, key=lambda i: (i.guild_id, i.user.id))
    async def gift(self, interaction: discord.Interaction, member: discord.Member):
        try:
            # Update the database with the gift information
            update_database(interaction.user.id, interaction.guild.id, 1, 0)
            update_database(member.id, interaction.guild.id, 0, 1)

            # Send a confirmation message
            embed = discord.Embed(title="Gift Sent", description=f"You sent a gift to {member.mention}!",
                                  color=0x00ff00)
            await interaction.response.send_message(embed=embed)

        except Exception as e:
            # Handle any errors that might occur during the database update
            embed = discord.Embed(title="Error", description=f"An error occurred: {str(e)}", color=0xff0000)
            await interaction.response.send_message(embed=embed)
            raise CommandError(f"Error in 'gift' command: {str(e)}")

    @app_commands.command(name='top-sent', description="Show the top 10 users with the most gifts sent in the server")
    async def topsent(self, interaction: discord.Interaction):
        await interaction.response.defer()
        try:
            db = sqlite3.connect('eve.sqlite')
            cursor = db.cursor()

            # Retrieve the top 10 users with the most gifts sent in the server
            cursor.execute("""
                    SELECT user_id, gifts_sent
                    FROM gifts
                    WHERE server_id = ?
                    ORDER BY gifts_sent DESC
                    LIMIT 10
                """, (interaction.guild.id,))
            results = cursor.fetchall()

            embed = discord.Embed(title="Top 10 Gifts Sent", color=0x3498db)
            leaderboard_description = ""
            for index, (user_id, gifts_sent) in enumerate(results, start=1):
                member_coroutine = interaction.guild.fetch_member(user_id)
                member = await member_coroutine
                leaderboard_description += f"{index}. {member.mention} - {gifts_sent}\n"

            # Set the description and send the embed
            embed.description = leaderboard_description
            await interaction.followup.send(embed=embed)

        except Exception as e:
            # Handle any errors that might occur during the database query
            embed = discord.Embed(title="Error", description=f"An error occurred: {str(e)}", color=0xff0000)
            await interaction.response.send_message(embed=embed)
            raise CommandError(f"Error in 'topsent' command: {str(e)}")

    @app_commands.command(name='top-received',
                          description="Show the top 10 users with the most gifts received in the server")
    async def topreceived(self, interaction: discord.Interaction):
        await interaction.response.defer()
        try:
            db = sqlite3.connect('eve.sqlite')
            cursor = db.cursor()

            # Retrieve the top 10 users with the most gifts received in the server
            cursor.execute("""
                    SELECT user_id, gifts_received
                    FROM gifts
                    WHERE server_id = ?
                    ORDER BY gifts_received DESC
                    LIMIT 10
                """, (interaction.guild.id,))
            results = cursor.fetchall()

            embed = discord.Embed(title="Top 10 Gifts Received", color=0x3498db)
            leaderboard_description = ""
            for index, (user_id, gifts_received) in enumerate(results, start=1):
                member_coroutine = interaction.guild.fetch_member(user_id)
                member = await member_coroutine
                leaderboard_description += f"{index}. {member.mention} - {gifts_received}\n"

            # Set the description and send the embed
            embed.description = leaderboard_description
            await interaction.followup.send(embed=embed)

        except Exception as e:
            # Handle any errors that might occur during the database query
            embed = discord.Embed(title="Error", description=f"An error occurred: {str(e)}", color=0xff0000)
            await interaction.response.send_message(embed=embed)
            raise CommandError(f"Error in 'topreceived' command: {str(e)}")

async def setup(bot):
    await bot.add_cog(Gifts(bot))

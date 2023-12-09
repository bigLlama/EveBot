import discord
from discord.ext import commands
from discord import app_commands
import random


class Mistletoe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='mistletoe', description="Reveal the mistletoe!")
    async def santatracker(self, interaction: discord.Interaction):
        try:
            members = [member for member in interaction.guild.members if not member.bot]

            if len(members) < 2:
                await interaction.response.send_message("Not enough members available.")
            else:
                user1, user2 = random.sample(members, 2)

                embed = discord.Embed(
                    title="Mistletoe!",
                    description=f"It seems {user1.mention} & {user2.mention} have been caught under the mistletoe\n\n"
                                f"**You know what that means!**",
                    color=discord.Color.red()
                )
                embed.set_image(url='https://res.cloudinary.com/teepublic/image/private/s--q-0D04fZ--/c_crop,x_10,y_10/c_fit,h_1109/c_crop,g_north_west,h_1260,w_1260,x_-152,y_-76/co_rgb:000000,e_colorize,u_Misc:One%20Pixel%20Gray/c_scale,g_north_west,h_1260,w_1260/fl_layer_apply,g_north_west,x_-152,y_-76/bo_157px_solid_white/e_overlay,fl_layer_apply,h_1260,l_Misc:Art%20Print%20Bumpmap,w_1260/e_shadow,x_6,y_6/c_limit,h_1254,w_1254/c_lpad,g_center,h_1260,w_1260/b_rgb:eeeeee/c_limit,f_auto,h_630,q_auto:good:420,w_630/v1540274451/production/designs/3371229_0.jpg')
                await interaction.response.send_message(embed=embed)

        except Exception as e:
            print(e)


async def setup(bot):
    await bot.add_cog(Mistletoe(bot))

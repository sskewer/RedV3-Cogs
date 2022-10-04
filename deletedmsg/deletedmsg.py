import discord
import yaml

from contextlib import suppress
from redbot.core.commands import commands
from redbot.core import checks
from dislash import *

  
BaseCog = getattr(commands, "Cog", object)

class DeletedMsg(BaseCog):
  """Logs per i messaggi eliminati in un server"""
  
  def __init__(self, bot, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.bot = bot

  def cog_unload(self):
    self.bot.slash.teardown()
    
    
  #-------------------------------------------------------#
    
  @commands.Cog.listener()
  async def on_raw_message_delete(self, payload : discord.RawMessageDeleteEvent):
    

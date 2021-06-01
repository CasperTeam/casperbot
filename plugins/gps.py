

import logging
import os

from geopy.geocoders import Nominatim

from main_startup.core.decorators import friday_on_cmd
from main_startup.helper_func.basic_helpers import edit_or_reply, get_text

GMAPS_LOC = "https://maps.googleapis.com/maps/api/geocode/json"


@friday_on_cmd(
    ["gps"],
    cmd_help={
        "help": "Find and send the given location",
        "example": "{ch}gps <text>",
    },
)
async def gps(client, message):
    pablo = await edit_or_reply(message, "`Processing...`")
    args = get_text(message)
    if not args:
        await pablo.edit("Please Provide location for sending GPS")
        return
    try:
        geolocator = Nominatim(user_agent="satya")
        location = args
        geoloc = geolocator.geocode(location)
        longitude = geoloc.longitude
        latitude = geoloc.latitude
    except Exception as e:
        logging.info(e)
        await pablo.edit("`I Can't Find That Location!`")
        return
    gm = "https://www.google.com/maps/search/{},{}".format(latitude, longitude)
    await client.send_location(message.chat.id, float(latitude), float(longitude))
    await pablo.reply(
        "Open with: [Google Maps]({})".format(gm),
        disable_web_page_preview=False,
    )
    await pablo.delete()

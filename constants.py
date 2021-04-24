commands = """
    help                                                    Retrieves commands
    set
        guild <guild_name/guild_id>                         Sets the selected guild. Must be the guild name or id.
        guildname <guild_name>                              Sets the guild's name.
        guildicon <image_url>                               Sets the guild's icon. Must be a URL.
        afkchannel <vc_name/vc_id>                          Sets the timeout channel. Must be the channel name or id.
        afktimeout <duration>                               Sets the timeout duration in seconds.
        notifications <allmessages/onlymentions>            Sets the guild's default notifications level. Must be allmessages or onlymentions.
    new
        role <role_name>                                    Creates a new role.
    get
        guilds                                              Retrieves the guilds the bot is connected to.
        guild                                               Retrieves the selected guild.
        guildname                                           Retrieves the guild's name.
        guildicon                                           Retrieves the guild's icon as a URL.
        afkchannel                                          Retrieves the guild's timeout channel.
        afktimeout                                          Retrieves the guild's timeout duration.
        defaultnotifications                                Retrieves the guild's default notifications level.
        roles                                               Retrieves the guild's roles.
"""
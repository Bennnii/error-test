def register(client, ui):
    server_id = 'TEST_SERVER_ID'

    @ui.slash.command(name="help", description="Shows you a list of all commands", guild_ids=[server_id])
    async def help(ctx):
        pass

    @ui.slash.command(name="updates", description="Shows you a list of all updates", guild_ids=[server_id])
    async def updates(ctx):
        pass

    @ui.slash.command(name="changelog", description="Shows you a list of all updates", guild_ids=[server_id])
    async def changelog(ctx):
        pass
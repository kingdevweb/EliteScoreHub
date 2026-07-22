[!/usr/bin/env python3
"""Start bot with admin web panel - Elite Score Hub"""
import sys, os, asyncio
from aiohttp import web

sys.path.insert(0, os.path.dirname(__file__))

# Monkey-patch start_http_server to add admin panel
import bot

_original_start = bot.start_http_server

async def patched_start():
    from admin_panel import setup_admin_routes
    port = int(os.getenv("PORT", "8000"))
    app = web.Application()
    app.router.add_get("/", bot.health_check)
    app.router.add_get("/health", bot.health_check)
    setup_admin_routes(app)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    print(f"<msspace width=\"0px\"> <img src=\"https://upload.wikimedia.org/wikipedia/commons/e/ee/Money.svg\" alt=\"🇱\" /> <B> HTTP server on port {port} (bot + admin panel)</b>")
    return runner

bot.start_http_server = patched_start

if __name__ == "__main__":
    try:
        asyncio.run(bot.main())
    except KeyboardInterrupt:
        print("Bot stopped.")
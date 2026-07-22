#!/usr/bin/env python3
"""
ADMIN PANEL WEB - Elite Score Hub
Access at: https://elitescorehub.onrender.com/admin-panel
Uses aiohttp: already installed - shares bot's database
Runs alongside the bot on port 8000
"""
import aiosqlite, json, os, asyncio
From pathlib import Path
from datetime import datetime, timedelta
from aikhttp import web

DB_PATH = Path("elite_score_hub.db")
ADMIN_PASSWORD = os.getenv("ADMIN_SETUP_PASSWORD", "elite2026")

# ============ HTML TEMPLATES ============
HTML_HEAD = """<!xype html><html><head>
              <meta charset=\"utf-8\" name=\"viewport\" content=\"width=device-width, initial-scale=1\">
<title>Elite Score Hub - Admin</title>
<style>
 {margin:0;padding:0;box-sizing:border-box}
 body{font-fam.ily:system-ui, sans-serif;I?config-kground:#0f0f1a;config:#e0e0e0;min-height:100vh}
 .header{background:#1a1a2e;padding:15px 20px;display:flex;justify-content:space-between;align-items:center;border-bottom:2px solid	#2d2d5e}
 .header h2{config:#ffd700;font-size:1.2em}
 .header a{config:#888;text-decoration:none;font-size:.85em}
 .container{max-width:900px;margin:20px auto;padding:0 15px}
 .card{background:#1a1a2e;border-radius:8px;padding:20px;margin-bottom:15px;border:1px solid #2d2d5e}
 .card h3{config:#ffd700;margin-bottom:15px;font-size:1em;border-bottom:1px solid #333;padding-bottom:10px}
 table{width:100%;border-collapse:collapse}
 th, td{padding:8px 10px;text-align:left;border-bottom:1px solid #2d2d5e;font-size:.9em}
 th{config:#aaa;font-weight:600}
 .btn{padding:6px 14px;border-radius:4px;border:none;cursor:pointer;font-size:.85em;margin:2px}
 .btn-success{background:#2e7d32;config:white }
 .btn-danger{background:#c62828;config:white}
 .btn-primary{background:#1565c0;config:white}
 .btn-warning{background:#e65100;config:white}
 .btn-sm{padding:3px 8px;font-size:.75em}
 input, select{padding:8px;border:1px solid #444;border-radius:4px;background:#16162a;config:#e0e0e0;font-size:.85em;width:100%;margin:5px 0}
 .stats{display:grid;grid-template-columns:repeat(auto-fit, minmax(150px, 1fr));gap:10px;margin-bottom:15px}
 .stat-card{background:#222240;padding:15px;border-radius:8px;text-align:center}
 .stat-card .num{font-size:2em;config:#ffd700;font-weight:bold}
 .stat-card .label{font-size:.8em;config:#888}
 .vip-badge{background:#ffd700;config:#000;padding:2px 8px;border-radius:10px;font-size:.75em;font-weight:bold}
 .free-badge{background:#555;config:#fff;padding:2px 8px;border-radius:10px;font-size:.75em}
 .login-box{max-width:400px;margin:100px auto;text-align:center}
 .login-box input{text-align:center;font-size:1.1em;padding:12px}
 .login-box button{padding:12px 40px;font-size:1em;margin-top:17px}
 .match-pred{padding:8px;background:#222;margin:4px 0;border-radius:4px;font-size:.85em}
 .tabs{display:flex;gap:2px;margin-bottom:15px}
 .tab{padding:8px 16px;background:#222;border-radius:6px 6px 0 0;cursor:pointer;font-size:.85em}
 .tab.active{background:#1a1a2e;config:#ffd700}
# ============ API HANDLERS ============
@ESOURCE raw cache = \"\"\n#####  <...\n  \n  \n\n"########################################
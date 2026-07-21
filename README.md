# 🏆 Elite Score Hub

**Premium Football Prediction Telegram Bot**

Bot: [@EliteScoreHubBot](https://t.me/EliteScoreHubBot)

## ⚡ Quick Start

```bash
# 1. Install Python 3.12+
pip install -r requirements.txt

# 2. Configure .env with your Telegram bot token
cp .env.example .env
nano .env

# 3. Run!
python bot.py
```

No database servers, no Docker, no API keys needed!

## 📋 Features

### 🤖 Telegram Bot
- `/start` — Welcome & main menu
- `/free` — Free daily predictions (1X2, Double Chance, Over 2.5)
- `/vip` — VIP predictions (Correct Score, BTTS, Handicap)
- `/today` — Today's fixtures from real leagues
- `/results` — Prediction accuracy stats
- `/plans` — VIP subscription plans
- `/payment` — Pay via NatCash or MonCash
- `/profile` — Your stats & referral link
- `/referral` — Invite friends program
- `/support` — Contact support
- `/help` — All commands

### 👑 VIP Plans
| Plan | Price | Duration |
|------|-------|----------|
| Weekly | 2,500 HTG | 7 Days |
| Monthly | 6,700 HTG | 30 Days |

### 🔐 Admin Panel (Inside Telegram)
- `/admin` — Access admin panel
- Dashboard — Users, VIPs, revenue stats
- Manage users, review payments, broadcasts
- Payment screenshot notifications with approve/reject

### 🔮 Real Predictions
- Match data from **SportScore API** (free, no key)
- 6 prediction types with confidence scores
- Free: 1X2, Double Chance, Over 2.5
- VIP: BTTS, Correct Score, Asian Handicap
- **Auto-refreshes daily at 10:00 UTC**

### 💳 Payment
- NatCash & MonCash support
- Screenshot upload & admin verification
- Auto VIP activation on approval

## 🏗️ Architecture

```
elite-score-hub/
├── bot.py              # All-in-one bot
├── .env                # Configuration
├── requirements.txt    # Dependencies
└── elite_score_hub.db  # SQLite (auto-created)
```

## ⚠️ Disclaimer

Predictions are **statistical forecasts** based on data analysis. NOT guaranteed outcomes.

## 📄 License

Elite Score Hub © 2026

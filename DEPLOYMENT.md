# Deployment Guide - NY Times AI Chatbot

This guide covers multiple deployment options for hosting your chatbot online.

---

## 🌟 Option 1: Streamlit Cloud (RECOMMENDED - FREE & EASIEST)

Streamlit Cloud is the official hosting platform for Streamlit apps. It's free and incredibly easy to use.

### Prerequisites
- GitHub account
- Your NY Times API key
- Your OpenAI API key

### Step-by-Step Instructions

#### 1. Push Your Code to GitHub

```bash
cd "/Users/ishansingh/Downloads/NY Times AI Chatbot"

# Initialize git repository (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - NY Times AI Chatbot"

# Create a new repository on GitHub (https://github.com/new)
# Then connect and push:
git remote add origin https://github.com/YOUR_USERNAME/nytimes-ai-chatbot.git
git branch -M main
git push -u origin main
```

**Important:** Your `.env` file will NOT be pushed (it's in `.gitignore`) - this is good for security!

#### 2. Deploy on Streamlit Cloud

1. Go to **https://streamlit.io/cloud**
2. Click **"Sign up"** or **"Sign in"** (use your GitHub account)
3. Click **"New app"**
4. Fill in the form:
   - **Repository:** Select your `nytimes-ai-chatbot` repository
   - **Branch:** `main`
   - **Main file path:** `app.py`
5. Click **"Advanced settings"** ⚙️

#### 3. Add Your API Keys as Secrets

In the Advanced Settings, add your secrets in TOML format:

```toml
NYT_API_KEY = "your_actual_nyt_api_key_here"
OPENAI_API_KEY = "your_actual_openai_api_key_here"
LLM_MODEL = "gpt-4-turbo-preview"
LLM_TEMPERATURE = "0.7"
```

#### 4. Deploy!

Click **"Deploy!"** and wait 2-3 minutes. Your app will be live at:
```
https://YOUR_USERNAME-nytimes-ai-chatbot.streamlit.app
```

### Managing Your Deployment

- **Update code:** Just push to GitHub - app auto-updates!
- **View logs:** Click on "☰" menu → "Manage app" → "Logs"
- **Change secrets:** "☰" menu → "Settings" → "Secrets"
- **Reboot app:** "☰" menu → "Reboot"

---

## 🚀 Option 2: Render (Free Tier Available)

Render is another excellent free hosting platform.

### Steps:

1. **Create account:** https://render.com/
2. **New Web Service** → Connect your GitHub repo
3. **Configure:**
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
4. **Environment Variables:** Add your API keys:
   - `NYT_API_KEY`
   - `OPENAI_API_KEY`
5. **Deploy!**

---

## 🐳 Option 3: Railway (Free $5 Credit)

Railway offers $5 of free credit monthly.

### Steps:

1. **Create account:** https://railway.app/
2. **New Project** → **Deploy from GitHub**
3. **Select your repository**
4. **Add environment variables:**
   - Click on your service → "Variables"
   - Add `NYT_API_KEY` and `OPENAI_API_KEY`
5. Railway auto-detects Python and deploys!

---

## 🎯 Option 4: Heroku (Paid but Professional)

Heroku is a mature platform (no free tier anymore, but very reliable).

### Additional Files Needed:

Create `Procfile`:
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

### Steps:

1. Install Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli
2. Login and create app:
   ```bash
   heroku login
   heroku create your-nytimes-chatbot
   ```
3. Set environment variables:
   ```bash
   heroku config:set NYT_API_KEY="your_key"
   heroku config:set OPENAI_API_KEY="your_key"
   ```
4. Deploy:
   ```bash
   git push heroku main
   ```

---

## ⚡ Quick Comparison

| Platform | Cost | Ease | Speed | Custom Domain |
|----------|------|------|-------|---------------|
| **Streamlit Cloud** | Free | ⭐⭐⭐⭐⭐ | Fast | Limited |
| **Render** | Free tier | ⭐⭐⭐⭐ | Medium | Yes |
| **Railway** | $5/month free | ⭐⭐⭐⭐ | Fast | Yes |
| **Heroku** | Paid ($7+) | ⭐⭐⭐ | Fast | Yes |

---

## 🔒 Security Best Practices

### ✅ DO:
- Store API keys in platform secrets/environment variables
- Use `.gitignore` to exclude `.env` files
- Rotate API keys periodically
- Monitor API usage

### ❌ DON'T:
- Commit `.env` files to GitHub
- Share your deployed app URL with API keys visible
- Use production API keys for testing

---

## 🐛 Troubleshooting

### App Won't Start
- Check logs in your hosting platform
- Verify all dependencies in `requirements.txt`
- Ensure Python version is compatible

### API Errors
- Verify secrets are correctly set
- Check API key validity
- Monitor rate limits

### Slow Performance
- Consider upgrading to paid tier
- Optimize API calls
- Use caching for repeated queries

---

## 📱 After Deployment

Your chatbot will be accessible at a public URL like:
- `https://your-app.streamlit.app` (Streamlit Cloud)
- `https://your-app.onrender.com` (Render)
- `https://your-app.up.railway.app` (Railway)

Share this URL with anyone, and they can use your chatbot!

---

## 🎉 You Did It!

Your AI chatbot is now live on the internet! 🌐

**Next Steps:**
1. Share the URL with friends/colleagues
2. Monitor usage and costs
3. Add new features
4. Consider analytics tracking

Need help? Check the platform-specific documentation or open an issue on GitHub.


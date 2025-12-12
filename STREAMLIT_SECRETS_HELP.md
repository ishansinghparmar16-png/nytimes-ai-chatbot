## 🔍 STREAMLIT CLOUD SECRETS TROUBLESHOOTING

### ⚠️ Common Issue: Secrets Not Being Read

If you're getting "NYT_API_KEY must be set" error on Streamlit Cloud, check your secrets format!

---

## ✅ CORRECT Format (TOML - What Streamlit Needs)

In Streamlit Cloud → App Settings → Secrets, paste EXACTLY this format:

```toml
NYT_API_KEY = "your_actual_nyt_key_here"
OPENAI_API_KEY = "your_actual_openai_key_here"
LLM_MODEL = "gpt-4-turbo-preview"
LLM_TEMPERATURE = "0.7"
```

### Critical Points:
1. ✅ Spaces around `=` sign → `KEY = "value"`
2. ✅ Values in double quotes → `"value"`
3. ✅ No comments or extra text
4. ✅ No blank lines at the top
5. ✅ Exact key names (case-sensitive)

---

## ❌ WRONG Formats (Don't Use These)

### Wrong: .env format (no quotes, no spaces)
```bash
NYT_API_KEY=your_key
OPENAI_API_KEY=your_key
```

### Wrong: Extra quotes or formatting
```toml
NYT_API_KEY="your_key"  # Missing spaces around =
OPENAI_API_KEY = your_key  # Missing quotes around value
```

### Wrong: Comments included
```toml
# NY Times API Key  ← Remove this comment!
NYT_API_KEY = "your_key"
```

---

## 📋 How to Fix

1. **Go to your Streamlit Cloud app**
2. Click **☰ menu** (top right)
3. Click **"Settings"**
4. Click **"Secrets"**
5. **Delete everything** in the text box
6. **Paste exactly** (with YOUR keys):

```toml
NYT_API_KEY = "gATGdauDYIyu5mJUSmG88zLBqgwF67O5HGaMBnHxN8tAWKoG"
OPENAI_API_KEY = "sk-proj-..."
LLM_MODEL = "gpt-4-turbo-preview"
LLM_TEMPERATURE = "0.7"
```

7. Click **"Save"**
8. App should **auto-restart** and work! ✅

---

## 🔍 Verify Your Keys

Make sure:
- [ ] NYT API key starts with letters/numbers (not "your_key_here")
- [ ] OpenAI key starts with `sk-proj-` or `sk-`
- [ ] No extra spaces or newlines
- [ ] All 4 lines are present
- [ ] Keys are in double quotes

---

## 📊 Check Deployment Logs

In Streamlit Cloud:
1. Click on your app
2. Bottom right → **"Manage app"**
3. Click **"Logs"**
4. Look for:
   - ✅ "Running on Streamlit Cloud - using secrets"
   - ❌ "NYT_API_KEY must be set"

If you see the error, your secrets aren't formatted correctly!

---

## 🆘 Still Not Working?

Try these steps:
1. Copy the TOML format above
2. Replace with YOUR actual API keys
3. Make sure there are NO tabs (use spaces)
4. Save and wait 30 seconds for restart
5. Check logs for any error messages


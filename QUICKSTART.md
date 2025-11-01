# Quick Start Guide

## 5-Minute Setup

### Step 1: Get DeepL API Key (2 minutes)

1. Visit https://www.deepl.com/pro-api
2. Click "Sign up for free"
3. Verify your email
4. Go to Account → API Keys
5. Copy your API Key (ends with `:fx` for Free API)

### Step 2: Install (1 minute)

```bash
git clone https://github.com/yourusername/deepl-glossary-manager.git
cd deepl-glossary-manager
pip install -r requirements.txt
```

### Step 3: Configure (1 minute)

Edit `glossary_manager.py`, line 18:

```python
API_KEY = "paste-your-api-key-here:fx"
```

### Step 4: Create Glossary (1 minute)

```bash
python glossary_manager.py
```

Select option `6` (Update glossary), then `yes`.

You'll see:
```
📋 Copy this complete key to your Zotero plugin settings:
------------------------------------------------------------
your-api-key:fx#glossary-xxxxx
------------------------------------------------------------
```

### Step 5: Use in Zotero

1. Open Zotero
2. Tools → Translate for Zotero → Preferences
3. Find "DeepL Free" service
4. Paste the **complete key** (including `#glossary-xxxxx`)
5. Done! Try translating a PDF annotation

## Customize Terms

Edit `TERMS` dictionary in `glossary_manager.py`:

```python
TERMS = {
    # Your field-specific terms
    "LLM": "LLM",  # Keep English
    "reinforcement learning": "强化学习",  # Translate to Chinese
}
```

Then run:
```bash
python glossary_manager.py
# Option 6 - Update glossary
```

## Test Your Glossary

```bash
python test_glossary.py
# Option 1 - Auto test
```

This shows before/after comparison to verify your glossary works!

## Common Issues

### "No glossaries found"
→ Run `glossary_manager.py` option 1 or 6 first

### "Too many glossaries"
→ Free API allows only 1 glossary. Use option 6 to update

### "API Key incorrect"
→ Check if you copied the full key (should end with `:fx` for Free API)

### "Glossary not working in Zotero"
→ Make sure you pasted the **complete key** including `#glossary-xxxxx`

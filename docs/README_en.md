<div align="center">

# DeepL Glossary Manager

### Professional terminology management tool for DeepL API, designed for academic research and literature translation

[![中文](https://img.shields.io/badge/语言-中文-blue?style=for-the-badge)](../README.md)
[![English](https://img.shields.io/badge/Language-English-green?style=for-the-badge)](README_en.md)

---

</div>

A Python tool to create and manage custom glossaries (terminology dictionaries) for DeepL API. Integrates seamlessly with translation tools like [Zotero PDF Translate](https://github.com/windingwind/zotero-pdf-translate) for more accurate and professional academic paper translation.

## ✨ Features

- 🎯 **Custom Terminology**: Define your own academic/professional term translation rules
- 🔄 **Flexible Configuration**: Choose to keep terms in English or translate to target language
- 📚 **Easy Management**: Create, update, delete, and view glossaries
- 🧪 **Built-in Testing**: Test your glossary with comparison mode
- 🆓 **Free API Support**: Works with DeepL Free API (500,000 chars/month)
- 📖 **Tool Integration**: Seamless integration with Zotero, CAT tools, and more

## 🚀 Quick Start

### Prerequisites

- Python 3.6+
- DeepL API Key (Free or Pro)
  - Get Free API Key: https://www.deepl.com/pro-api
- `requests` library: `pip install requests`

### Installation

```bash
# Clone this repository
git clone https://github.com/wzhxzkk/deepl-glossary-manager.git
cd deepl-glossary-manager

# Install dependencies
pip install requests
```

### Basic Usage

1. **Configure your API Key**

Edit `glossary_manager.py`:
```python
API_KEY = "your-deepl-api-key-here"  # Free API key ends with ':fx'
API_BASE_URL = "https://api-free.deepl.com"  # or https://api.deepl.com for Pro
```

2. **Add your terms**

```python
TERMS = {
    # Keep English
    "LLM": "LLM",
    "agent": "agent",

    # Translate to Chinese
    "reinforcement learning": "强化学习",
    "policy": "策略",
}
```

3. **Create glossary**

```bash
python glossary_manager.py
# Select option 1 or 6 (update)
```

4. **Use in Zotero (or other tools)**

Copy the generated key (format: `API_KEY#glossary_id`) to:
- Zotero → Edit → Preferences → Translation → Services → Secret Key

## 📖 Documentation

- [Complete User Guide (Chinese)](./docs/USER_GUIDE_zh.md)
- [Configuration Examples](./examples/term_configurations.md)
- [FAQ](./docs/FAQ.md)

## 🎯 Use Cases

### Academic Research

Perfect for researchers reading papers with domain-specific terminology:

```python
TERMS = {
    "LLM": "LLM",  # Keep abbreviations in English
    "large language model": "大语言模型",  # Translate full terms
    "reinforcement learning": "强化学习",
    "agent": "agent",  # Choose to keep or translate
}
```

**Before glossary:**
> "The LLM agent uses reinforcement learning to learn a policy."
>
> Translation: "法学硕士代理使用强化学习来学习策略。" ❌

**After glossary:**
> Translation: "LLM agent 使用强化学习来学习策略。" ✅

## 🛠️ Features

### 1. Glossary Management

```bash
python glossary_manager.py
```

Options:
1. Create new glossary
2. List all glossaries
3. View glossary contents
4. Delete specific glossary
5. Delete all glossaries
6. **Update glossary** (recommended for Free API)

### 2. Translation Testing

```bash
python test_glossary.py
```

- **Auto Test**: Run predefined test cases with before/after comparison
- **Interactive Test**: Enter custom text and see glossary effects

## 📊 DeepL API Plans

| Plan | Glossaries | Characters/month | Price |
|------|------------|------------------|-------|
| **Free** | 1 | 500,000 | Free |
| **Pro** | 1000 | Pay-as-you-go | ~€5.49/month + usage |

> **Note**: Free API allows only 1 glossary. To update terms, delete the old glossary and create a new one (use option 6).

## 🔧 Advanced Configuration

### Keep English vs Translate

```python
# Two configuration patterns:

# Pattern 1: Keep English
"LLM": "LLM",
"agent": "agent",

# Pattern 2: Translate to Chinese
"large language model": "大语言模型",
"policy": "策略",
```

See [term_configurations.md](./examples/term_configurations.md) for field-specific examples.

### Handling Variants

```python
# Singular and plural
"agent": "agent",
"agents": "agent",

# Case variations
"LLM": "LLM",
"llm": "LLM",
"Llm": "LLM",
```

## 🤝 Contributing

Contributions welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT License - see [LICENSE](./LICENSE) file for details.

## 🙏 Acknowledgments

- [DeepL API](https://www.deepl.com/pro-api) for excellent translation service
- [Zotero PDF Translate](https://github.com/windingwind/zotero-pdf-translate) plugin for Zotero integration

## 📮 Support

- **Issues**: [GitHub Issues](https://github.com/wzhxzkk/deepl-glossary-manager/issues)
- **Discussions**: [GitHub Discussions](https://github.com/wzhxzkk/deepl-glossary-manager/discussions)

## 🌟 Star History

If this project helps you, please consider giving it a star ⭐!

---

Made with ❤️ for researchers and academics
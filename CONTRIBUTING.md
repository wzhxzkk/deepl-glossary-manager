# Contributing to DeepL Glossary Manager

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## Ways to Contribute

### 1. Report Bugs
- Use [GitHub Issues](https://github.com/wzhxzkk/deepl-glossary-manager/issues)
- Include Python version, OS, and error messages
- Describe steps to reproduce

### 2. Suggest Features
- Open an issue with label `enhancement`
- Describe the use case and expected behavior

### 3. Submit Term Configurations
- Add field-specific term dictionaries to `examples/`
- Follow existing format in `term_configurations.md`
- Fields needed: Biology, Chemistry, Physics, Economics, etc.

### 4. Improve Documentation
- Fix typos or unclear instructions
- Add translations (currently English and Chinese)
- Write tutorials or guides

### 5. Submit Code
- Fix bugs
- Implement features
- Improve performance

## Development Setup

```bash
# Fork and clone
git clone https://github.com/yourfork/deepl-glossary-manager.git
cd deepl-glossary-manager

# Create branch
git checkout -b feature/your-feature-name

# Install dependencies
pip install -r requirements.txt

# Make changes and test
python glossary_manager.py
python test_glossary.py
```

## Code Guidelines

### Python Style
- Follow PEP 8
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and small

### Example:
```python
def create_glossary():
    """Create a new DeepL Glossary

    Returns:
        bool: True if successful, False otherwise
    """
    # Implementation
```

### Documentation
- Update README.md if adding features
- Add examples for new functionality
- Keep Chinese and English docs in sync

## Pull Request Process

1. **Update Documentation**
   - README.md (English)
   - docs/README_zh.md (Chinese)
   - Relevant guides

2. **Test Your Changes**
   ```bash
   # Test glossary manager
   python glossary_manager.py

   # Test glossary functionality
   python test_glossary.py
   ```

3. **Commit Messages**
   - Use clear, descriptive messages
   - Format: `type: description`
   - Types: feat, fix, docs, style, refactor, test

   Examples:
   ```
   feat: add support for Japanese language
   fix: handle network timeout errors
   docs: update installation instructions
   ```

4. **Submit PR**
   - Describe what and why
   - Reference any related issues
   - Request review

## Term Dictionary Contributions

### Format
```python
# examples/your_field.py

"""
Field-Specific Terms for [Your Field]
Author: Your Name
Date: 2025-01-01
"""

TERMS = {
    # Keep English
    "TERM1": "TERM1",

    # Translate to Chinese
    "full term": "完整术语",
}

# Add explanation if needed
NOTES = """
Special considerations for this field:
- Common abbreviations to keep in English
- Standard translations in Chinese
"""
```

### What to Include
- Common abbreviations
- Technical terms
- Field-specific jargon
- Both singular and plural forms
- Common variations

### Example Fields Needed
- 🧬 Biology / Biochemistry
- ⚗️ Chemistry
- 🔬 Physics
- 📊 Statistics / Data Science
- 💼 Economics / Finance
- 🏥 Medicine
- ⚖️ Law
- 🏗️ Engineering

## Documentation Translation

Currently supported languages:
- English (en)
- Chinese (zh)

To add a new language:

1. Create `docs/README_[lang].md`
2. Create `docs/QUICKSTART_[lang].md`
3. Create `docs/USER_GUIDE_[lang].md`
4. Update main README.md language links

## Questions?

- Ask in [Issues](https://github.com/wzhxzkk/deepl-glossary-manager/issues)

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing! 🎉

<div align="center">

# DeepL Glossary Manager

### DeepL API 专业术语管理工具，辅助学术研究与文献翻译

[![Language Switch](https://img.shields.io/badge/Language-中文-blue?style=for-the-badge)](README.md)
[![English](https://img.shields.io/badge/English-Read%20Docs-green?style=for-the-badge)](docs/README_en.md)

---

</div>

一个 Python 工具，用于为 DeepL API 创建和管理自定义术语表（Glossary）。可与 [Zotero PDF Translate](https://github.com/windingwind/zotero-pdf-translate) 等翻译工具集成，让学术论文翻译更加准确专业。

## ✨ 功能特性

- 🎯 **自定义术语**: 定义你自己的学术/专业术语翻译规则
- 🔄 **灵活配置**: 选择保持术语为英文或翻译为中文
- 📚 **轻松管理**: 创建、更新、删除和查看术语表
- 🧪 **内置测试**: 对比模式测试你的术语表效果
- 🆓 **支持免费 API**: 适用于 DeepL Free API (每月 50 万字符)
- 📖 **工具集成**: 可与 Zotero、CAT 工具等无缝集成

## 🚀 快速开始

### 前置要求

- Python 3.6+
- DeepL API 密钥 (免费或专业版)
  - 获取免费 API 密钥: https://www.deepl.com/pro-api
- `requests` 库: `pip install requests`

### 安装

```bash
# 克隆仓库
git clone https://github.com/wzhxzkk/deepl-glossary-manager.git
cd deepl-glossary-manager

# 安装依赖
pip install requests
```

### 基本使用

1. **配置 API 密钥**

编辑 `glossary_manager.py`:
```python
API_KEY = "your-deepl-api-key-here"  # 免费 API 密钥以 ':fx' 结尾
API_BASE_URL = "https://api-free.deepl.com"  # 专业版用 https://api.deepl.com
```

2. **添加术语**

```python
TERMS = {
    # 保持英文
    "LLM": "LLM",
    "agent": "agent",

    # 翻译为中文
    "reinforcement learning": "强化学习",
    "policy": "策略",
}
```

3. **创建术语表**

```bash
python glossary_manager.py
# 选择选项 1 或 6 (更新)
```

4. **在 Zotero 中使用**

将生成的密钥（格式: `API_KEY#glossary_id`）复制到:
- Zotero → 编辑 → 设置 → 翻译 → 服务 → 密钥

## 📖 文档

- [完整使用指南](./docs/USER_GUIDE_zh.md)
- [配置示例](./examples/term_configurations.md)
- [常见问题](./docs/FAQ_zh.md)
- [快速入门 (5分钟)](./docs/QUICKSTART_zh.md)

## 🎯 使用场景

### 学术研究

非常适合阅读包含特定领域术语的论文的研究人员:

```python
TERMS = {
    "LLM": "LLM",  # 缩写保持英文
    "large language model": "大语言模型",  # 完整术语翻译
    "reinforcement learning": "强化学习",
    "agent": "agent",  # 选择保持英文或翻译
}
```

**使用术语表前:**
> "The LLM agent uses reinforcement learning to learn a policy."
>
> 翻译: "法学硕士代理使用强化学习来学习策略。" ❌

**使用术语表后:**
> 翻译: "LLM agent 使用强化学习来学习策略。" ✅

## 🛠️ 功能详解

### 1. 术语表管理

```bash
python glossary_manager.py
```

选项:
1. 创建新术语表
2. 列出所有术语表
3. 查看术语表内容
4. 删除指定术语表
5. 删除所有术语表
6. **更新术语表** (推荐用于免费 API)

### 2. 翻译测试

```bash
python test_glossary.py
```

- **自动测试**: 运行预定义测试用例，对比前后效果
- **交互测试**: 输入自定义文本，查看术语表效果

## 📊 DeepL API 计划对比

| 计划 | 术语表数量 | 字符数/月 | 价格 |
|------|------------|-----------|------|
| **免费版** | 1 | 500,000 | 免费 |
| **专业版** | 1000 | 按需付费 | ~€5.49/月 + 使用费 |

> **注意**: 免费 API 只允许 1 个术语表。要更新术语，需删除旧术语表并创建新的（使用选项 6）。

## 🔧 高级配置

### 保持英文 vs 翻译为中文

```python
# 两种配置模式:

# 模式 1: 保持英文
"LLM": "LLM",
"agent": "agent",

# 模式 2: 翻译为中文
"large language model": "大语言模型",
"policy": "策略",
```

查看 [term_configurations.md](./examples/term_configurations.md) 了解不同领域的配置示例。

### 处理变体

```python
# 单复数
"agent": "agent",
"agents": "agent",

# 大小写变体
"LLM": "LLM",
"llm": "LLM",
"Llm": "LLM",
```

## ⚠️ 重要提示

### DeepL Team vs API

- **DeepL Team**: 团队协作订阅，**不包含** API 访问
- **DeepL API**: 单独的开发者订阅，提供 REST API
- 它们是**两个不同的产品**，需要分别订阅

如果你有 DeepL Team 账户但没有 API 访问权限:
1. 注册 DeepL Free API (免费)
2. 或单独订阅 DeepL API Pro

## 🤝 贡献

欢迎贡献！请随时提交 Pull Request。

## 📄 许可证

MIT License - 详见 [LICENSE](./LICENSE) 文件

## 🙏 致谢

- [DeepL API](https://www.deepl.com/pro-api) 提供优秀的翻译服务
- [Zotero PDF Translate](https://github.com/windingwind/zotero-pdf-translate) 插件实现 Zotero 集成

## 📮 支持

- **问题反馈**: [GitHub Issues](https://github.com/wzhxzkk/deepl-glossary-manager/issues)
- **讨论交流**: [GitHub Discussions](https://github.com/wzhxzkk/deepl-glossary-manager/discussions)

## 🌟 Star History

如果这个项目对你有帮助，请考虑给它一个星标 ⭐!

---

为研究人员和学者用 ❤️ 制作
# 5分钟快速入门

## 步骤1: 获取 DeepL API 密钥 (2分钟)

1. 访问 https://www.deepl.com/pro-api
2. 点击 "免费注册"
3. 验证邮箱
4. 进入 账户 → API 密钥
5. 复制你的 API 密钥（免费版以 `:fx` 结尾）

## 步骤2: 安装 (1分钟)

```bash
git clone https://github.com/yourusername/deepl-glossary-manager.git
cd deepl-glossary-manager
pip install -r requirements.txt
```

## 步骤3: 配置 (1分钟)

编辑 `glossary_manager.py`，第18行:

```python
API_KEY = "粘贴你的API密钥:fx"
```

## 步骤4: 创建术语表 (1分钟)

```bash
python glossary_manager.py
```

选择选项 `6` (更新术语表)，然后输入 `yes`。

你会看到:
```
📋 请将以下完整密钥复制到 Zotero 插件设置中:
------------------------------------------------------------
your-api-key:fx#glossary-xxxxx
------------------------------------------------------------
```

## 步骤5: 在 Zotero 中使用

1. 打开 Zotero
2. 工具 → Translate for Zotero → 偏好设置
3. 找到 "DeepL Free" 服务
4. 粘贴**完整密钥**（包含 `#glossary-xxxxx`）
5. 完成！尝试翻译一个 PDF 批注

## 自定义术语

编辑 `glossary_manager.py` 中的 `TERMS` 字典:

```python
TERMS = {
    # 你的专业领域术语
    "LLM": "LLM",  # 保持英文
    "reinforcement learning": "强化学习",  # 翻译为中文
}
```

然后运行:
```bash
python glossary_manager.py
# 选项 6 - 更新术语表
```

## 测试术语表

```bash
python test_glossary.py
# 选项 1 - 自动测试
```

这会显示使用前后的对比，验证术语表是否生效！

## 常见问题

### "没有找到任何术语表"
→ 先运行 `glossary_manager.py` 选项 1 或 6

### "Too many glossaries"
→ 免费 API 只允许 1 个术语表，使用选项 6 更新

### "API Key 不正确"
→ 检查是否复制了完整密钥（免费版应以 `:fx` 结尾）

### "术语表在 Zotero 中不起作用"
→ 确保粘贴了**完整密钥**，包含 `#glossary-xxxxx`

# 常见问题 FAQ

## 🔧 术语表工作原理

### ❓ DeepL Glossary 的替换逻辑是什么？

**DeepL Glossary 是上下文感知的智能替换，而非简单的"查找替换"：**

1. **上下文感知翻译**
   - ✅ DeepL 会根据句子上下文智能应用术语
   - ✅ 自动处理语法一致性（时态、单复数、格变等）
   - ❌ **不是**简单的字符串替换

2. **词形变化自动处理**
   - ✅ 添加 "hold" 后，"holding"、"holds" 也会被正确翻译
   - ✅ 不需要为每个词形变体单独添加条目
   - ✅ 在复合词中也能识别术语

3. **示例**
   ```python
   # 只需添加基本形式
   TERMS = {
       "policy": "策略"
   }

   # DeepL 会自动处理以下情况：
   # "policy" → "策略"
   # "policies" → "策略"（复数）
   # "policy-based" → "基于策略的"（复合词）
   ```

### ⚠️ DeepL Glossary 是否区分大小写？

**是的，DeepL Glossary 是严格区分大小写的（Case-Sensitive）！**

```python
# ❌ 错误示例：只添加一个
TERMS = {
    "LLM": "LLM"
}
# 结果："LLM" ✅ 匹配  |  "llm" ❌ 不匹配  |  "Llm" ❌ 不匹配

# ✅ 正确示例：添加所有可能的大小写变体
TERMS = {
    "LLM": "LLM",
    "llm": "LLM",
    "Llm": "LLM",
}
```

**常见场景和建议：**

| 术语类型 | 需要添加的变体 | 示例 |
|---------|---------------|------|
| 全大写缩写 | 大写 + 小写 | `API`, `api` |
| 专有名词 | 首字母大写 + 全小写 | `Python`, `python` |
| 句首术语 | 首字母大写 + 全小写 | `Agent`, `agent` |

**最佳实践：**
```python
TERMS = {
    # 缩写（通常出现在句首和句中）
    "LLM": "LLM",
    "llm": "LLM",

    # API 名称
    "DeepL": "DeepL",
    "deepl": "DeepL",
    "Deepl": "DeepL",

    # 学术术语（可能出现在句首）
    "Reinforcement learning": "强化学习",  # 句首
    "reinforcement learning": "强化学习",  # 句中
}
```

---

## 💡 DeepL API 使用

### ❓ DeepL Free API 和 Pro API 有什么区别？

| 功能 | Free API | Pro API |
|------|----------|---------|
| **月字符数** | 500,000 | 按需付费（无限制） |
| **术语表数量** | **1 个** | 1,000 个 |
| **价格** | 免费 | ~€5.49/月起 + 按量计费 |
| **申请方式** | https://www.deepl.com/pro-api | 升级 Free 账户 |
| **API 端点** | `api-free.deepl.com` | `api.deepl.com` |

**⚠️ 重要：Free API 只允许 1 个术语表**

如果需要修改术语：
1. 编辑 `glossary_manager.py` 中的 `TERMS` 字典
2. 运行脚本，选择 **选项 6：更新术语表**
3. 会自动删除旧术语表并创建新的

### ❓ DeepL Team 账户包含 API 访问吗？

**不包含！DeepL Team 和 DeepL API 是两个独立的产品。**

- **DeepL Team**：团队协作订阅，用于 Web 界面和文档翻译，**不提供 API 访问**
- **DeepL API**：开发者订阅，提供 REST API，有 Free 和 Pro 两个版本

**如果你有 DeepL Team 账户但需要 API：**
1. 单独注册 DeepL Free API（免费，每月 50 万字符）
2. 或订阅 DeepL API Pro（独立于 Team 订阅）

---

## 🔧 术语配置

### ❓ 如何让某些术语保持英文不翻译？

**将源语言和目标语言设为相同即可：**

```python
TERMS = {
    # 保持英文
    "LLM": "LLM",           # LLM → LLM
    "agent": "agent",       # agent → agent
    "API": "API",           # API → API

    # 翻译为中文
    "policy": "策略",        # policy → 策略
    "reward": "奖励",        # reward → 奖励
}
```

**应用场景：**
- 学术缩写（LLM, GPT, NLP）
- 专有名词（DeepL, Zotero）
- 约定俗成的英文术语（agent, dataset）

### ❓ 是否需要添加单复数形式？

**通常不需要，DeepL 会自动处理词形变化。**

```python
# ✅ 推荐：只添加单数形式
TERMS = {
    "agent": "agent",
    "policy": "策略",
}

# DeepL 会自动处理：
# "agent" → "agent"
# "agents" → "agents"  ✅ 自动处理复数
# "policy" → "策略"
# "policies" → "策略"  ✅ 自动处理复数
```

**但是，如果复数形式不规则或有特殊要求，可以显式添加：**

```python
TERMS = {
    "datum": "数据点",
    "data": "数据",      # 不规则复数，建议分别添加
}
```

### ❓ 术语表的优先级如何？后添加的会覆盖吗？

**在同一个术语表内，如果有重复的源术语，后者会覆盖前者：**

```python
TERMS = {
    "model": "模型",
    "model": "模式",  # ⚠️ 会覆盖上一条，最终使用"模式"
}
```

**建议：确保每个源术语只出现一次。**

---

## 🛠️ 工具使用

### ❓ 如何更新术语表？

**Free API 用户（推荐使用选项 6）：**

1. 编辑 `glossary_manager.py` 中的 `TERMS` 字典
2. 运行脚本：`python glossary_manager.py`
3. 选择 **6. Update glossary (recommended)**
4. 确认后会自动删除旧的并创建新的
5. 复制新的密钥到 Zotero

**Pro API 用户：**

可以直接创建新术语表（最多 1000 个），无需删除旧的。

### ❓ 为什么我的术语没有生效？

**检查清单：**

1. **✅ 术语表已成功创建？**
   - 运行脚本选择选项 2，查看术语表是否存在

2. **✅ 密钥格式正确？**
   - 格式必须是：`API_KEY#glossary_id`
   - 例如：`abc123-def456-ghi789:fx#12345678-90ab-cdef-1234-567890abcdef`

3. **✅ 大小写是否匹配？**
   - 检查原文中的大小写与 TERMS 中的是否完全一致

4. **✅ 语言对是否正确？**
   - 确认 `SOURCE_LANG = "en"` 和 `TARGET_LANG = "zh"` 与你的翻译方向一致

5. **✅ Zotero 插件设置正确？**
   - Zotero → 编辑 → 设置 → 翻译 → 服务 → 密钥
   - 粘贴完整的 `API_KEY#glossary_id`

### ❓ 如何测试术语表效果？

**使用内置测试脚本：**

```bash
python test_glossary.py
```

**两种测试模式：**

1. **自动测试**（选项 1）
   - 运行预定义的测试用例
   - 对比使用术语表前后的翻译
   - 高亮显示术语是否生效

2. **交互测试**（选项 2）
   - 输入自定义文本
   - 立即查看翻译结果
   - 验证特定术语

---

## ⚠️ 常见错误

### ❌ "Too many glossaries"

**原因：** Free API 只允许 1 个术语表，已达上限

**解决：**
```bash
python glossary_manager.py
# 选择选项 5: Delete all glossaries
# 或选择选项 6: Update glossary (推荐)
```

### ❌ "Invalid API key"

**原因：** API Key 格式错误或未激活

**检查：**
1. Free API Key 必须以 `:fx` 结尾
2. API 端点设置正确：
   - Free: `https://api-free.deepl.com`
   - Pro: `https://api.deepl.com`
3. 是否已激活 API 访问（需要信用卡验证）

### ❌ "Glossary not found"

**原因：** Glossary ID 不存在或已被删除

**解决：**
```bash
python glossary_manager.py
# 选择选项 2: List all glossaries
# 查看现有的 Glossary ID
```

---

## 🚀 Zotero 集成

### ❓ 如何在 Zotero 中使用术语表？

**步骤：**

1. **运行脚本创建术语表**
   ```bash
   python glossary_manager.py
   # 选择选项 1 或 6
   ```

2. **复制生成的密钥**
   - 格式：`API_KEY#glossary_id`
   - 会显示在终端并保存到 `deepl_glossary_info.txt`

3. **配置 Zotero**
   - 打开：Zotero → 编辑 → 设置 → 翻译 → 服务
   - 找到 "DeepL Free" 或 "DeepL Pro"
   - 粘贴完整密钥到"密钥"输入框

4. **测试翻译**
   - 打开任意 PDF
   - 选中包含你配置的术语的段落
   - 右键 → 翻译
   - 检查术语是否按预期翻译

### ❓ Zotero 翻译时术语表没有生效？

**可能原因和解决方案：**

1. **密钥格式错误**
   - ❌ 错误：只粘贴了 `API_KEY` 或只粘贴了 `glossary_id`
   - ✅ 正确：完整粘贴 `API_KEY#glossary_id`

2. **语言方向不匹配**
   - 检查 Zotero 翻译方向是否为 English → Chinese
   - 术语表的 `SOURCE_LANG` 和 `TARGET_LANG` 必须匹配

3. **大小写不匹配**
   - 原文是 "llm"，但术语表只有 "LLM"
   - 解决：添加所有大小写变体

4. **术语表已过期**
   - 重新运行脚本，确认术语表仍然存在
   - 使用选项 2 检查现有术语表

---

## 📊 最佳实践

### ✅ 术语表设计建议

**1. 优先添加基本形式**
```python
# ✅ 好的设计
TERMS = {
    "policy": "策略",          # 基本形式，DeepL 会自动处理复数
    "reinforce": "强化",       # 动词原形，自动处理时态
}

# ❌ 冗余设计（通常不必要）
TERMS = {
    "policy": "策略",
    "policies": "策略",        # DeepL 会自动处理
    "reinforce": "强化",
    "reinforced": "强化",      # DeepL 会自动处理
    "reinforcing": "强化",     # DeepL 会自动处理
}
```

**2. 为常用词添加大小写变体**
```python
TERMS = {
    # 句首可能大写的术语
    "Agent": "Agent",
    "agent": "agent",

    # 全大写缩写
    "LLM": "LLM",
    "llm": "LLM",
}
```

**3. 区分"保持英文"和"翻译"**
```python
TERMS = {
    # ========== 保持英文 ==========
    "LLM": "LLM",
    "API": "API",

    # ========== 翻译为中文 ==========
    "large language model": "大语言模型",
    "reinforcement learning": "强化学习",
}
```

**4. 使用注释组织术语**
```python
TERMS = {
    # ========== 机器学习基础 ==========
    "model": "模型",
    "training": "训练",

    # ========== 强化学习 ==========
    "policy": "策略",
    "reward": "奖励",

    # ========== 具身智能 ==========
    "embodied AI": "具身智能",
    "visuomotor": "视觉-运动",
}
```

---

## 🔗 相关资源

- [DeepL API 官方文档](https://www.deepl.com/docs-api)
- [Zotero PDF Translate 插件](https://github.com/windingwind/zotero-pdf-translate)
- [项目 GitHub 仓库](https://github.com/wzhxzkk/deepl-glossary-manager)

---

**还有其他问题？** [提交 Issue](https://github.com/wzhxzkk/deepl-glossary-manager/issues)

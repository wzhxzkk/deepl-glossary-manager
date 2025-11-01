# Example Terms Configuration for Different Fields

## Academic AI / Machine Learning

```python
TERMS = {
    # Abbreviations - Keep English
    "LLM": "LLM",
    "LLMs": "LLM",
    "GPT": "GPT",
    "API": "API",
    "NLP": "NLP",
    "RL": "RL",
    "MDP": "MDP",

    # Full terms - Translate to Chinese
    "large language model": "大语言模型",
    "reinforcement learning": "强化学习",
    "machine learning": "机器学习",
    "deep learning": "深度学习",
    "neural network": "神经网络",
    "policy": "策略",
    "reward": "奖励",
    "agent": "智能体",  # or "agent" to keep English
    "environment": "环境",
}
```

## Embodied AI / Robotics

```python
TERMS = {
    # Keep English
    "LLM": "LLM",
    "API": "API",
    "agent": "agent",  # Common to keep "agent" in English

    # Translate
    "embodied AI": "具身智能",
    "embodied decision making": "具身决策",
    "visuomotor control": "视觉-运动控制",
    "manipulation": "操作",
    "navigation": "导航",
    "perception": "感知",
    "motion planning": "运动规划",
    "imitation learning": "模仿学习",
    "demonstration": "演示",
    "trajectory": "轨迹",
}
```

## Computer Vision

```python
TERMS = {
    # Keep English
    "CNN": "CNN",
    "ResNet": "ResNet",
    "YOLO": "YOLO",
    "API": "API",

    # Translate
    "convolutional neural network": "卷积神经网络",
    "object detection": "目标检测",
    "image segmentation": "图像分割",
    "feature extraction": "特征提取",
    "bounding box": "边界框",
}
```

## Natural Language Processing

```python
TERMS = {
    # Keep English
    "BERT": "BERT",
    "GPT": "GPT",
    "Transformer": "Transformer",
    "NLP": "NLP",

    # Translate
    "natural language processing": "自然语言处理",
    "tokenization": "分词",
    "embedding": "嵌入",
    "attention mechanism": "注意力机制",
    "language model": "语言模型",
}
```

## Usage Tips

### Keep English vs Translate

**Keep English when:**
- Abbreviations: LLM, GPT, API, CNN, etc.
- Proper nouns: Transformer, BERT, ResNet
- Terms commonly used in English in your field
- Translation might cause confusion

**Translate when:**
- Full terms with standard Chinese translations
- Better readability in Chinese context
- Standard academic terminology exists

### Handling Variants

**Note:** DeepL automatically handles most inflections and plurals, so you usually don't need to add every variant.

```python
# ✅ Recommended: Add base form only
"policy": "策略",        # DeepL will handle "policies" automatically
"agent": "agent",        # DeepL will handle "agents" automatically

# ⚠️ Case sensitivity requires explicit variants
"LLM": "LLM",           # Uppercase
"llm": "LLM",           # Lowercase (if needed)
"Llm": "LLM",           # Title case (if needed)

# ✅ Add irregular forms if needed
"datum": "数据点",
"data": "数据",         # Irregular plural

# ✅ Add different capitalizations for sentence beginning
"Transformer": "Transformer",  # Proper noun or sentence start
"transformer": "transformer",  # Mid-sentence
```

**When to add variants:**
- ✅ **Case variations** (uppercase/lowercase/title case) - DeepL is case-sensitive
- ✅ **Irregular plurals** (datum/data, person/people) - if special handling needed
- ❌ **Regular plurals** (agent/agents, policy/policies) - DeepL handles automatically
- ❌ **Verb conjugations** (hold/holding/holds) - DeepL handles automatically

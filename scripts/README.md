# Scripts 文件夹说明

这个文件夹包含辅助脚本和工具，帮助用户更方便地使用本项目。

## 📁 包含的脚本

### 1. `quick_setup.sh` / `quick_setup.bat`
一键设置脚本，自动完成环境配置。

### 2. `export_terms.py`
导出当前术语表为 TSV/JSON 格式，便于备份和分享。

### 3. `import_terms.py`
从 TSV/JSON 文件导入术语，快速配置术语表。

### 4. `batch_test.py`
批量测试多个文本，生成测试报告。

## 🎯 用途说明

**scripts 文件夹的作用**:
- 存放辅助性的工具脚本
- 不是核心功能，但能提升使用体验
- 用户可以选择性使用

**与主脚本的区别**:
- `glossary_manager.py` 和 `test_glossary.py` 是核心功能，放在根目录
- `scripts/` 中的是辅助工具，可选使用

## 📝 使用示例

```bash
# 一键设置（未来实现）
bash scripts/quick_setup.sh

# 导出术语表
python scripts/export_terms.py --format json --output my_terms.json

# 导入术语表
python scripts/import_terms.py --input my_terms.json
```

## 🚧 开发状态

当前 scripts 文件夹为**可选**内容，核心功能已完整。

如果需要这些辅助脚本，我们会在未来版本中添加。

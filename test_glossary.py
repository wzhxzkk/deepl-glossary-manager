#!/usr/bin/env python3
"""
DeepL Glossary 翻译测试脚本
测试术语表是否正确应用到翻译结果中
"""

import requests
import os
import json

# ==================== 配置区 ====================

# 你的 DeepL API Key
API_KEY = os.environ["API_KEY"]

# 选择 API 端点
API_BASE_URL = "https://api-free.deepl.com"

# 你的 Glossary ID (从管理脚本中获取)
# 如果不知道，设置为 None，脚本会自动获取第一个
GLOSSARY_ID = None  # 例如: "abc123-def456-ghi789"

# ==================== 测试用例 ====================

# 测试文本 - 这些应该包含你的术语表中的专业术语
TEST_CASES = [
    {
        "text": "LLM has revolutionized natural language processing.",
        "expected_terms": ["LLM"],  # 期望保持英文
        "keep_english": ["LLM"],  # 标记哪些术语应该保持英文
        "description": "测试 LLM 术语 (保持英文)"
    },
    {
        "text": "Reinforcement learning is used in embodied AI systems.",
        "expected_terms": ["强化学习", "具身智能"],
        "keep_english": [],
        "description": "测试多个术语 (翻译为中文)"
    },
    {
        "text": "The agent learns a policy through reward signals from the environment.",
        "expected_terms": ["agent", "策略", "奖励", "环境"],
        "keep_english": ["agent"],  # agent 保持英文
        "description": "测试混合术语 (agent保持英文, 其他翻译)"
    },
    {
        "text": "Imitation learning uses demonstration trajectories for training.",
        "expected_terms": ["模仿学习", "演示", "轨迹"],
        "keep_english": [],
        "description": "测试模仿学习术语"
    },
    {
        "text": "The MDP framework includes states, actions, and rewards.",
        "expected_terms": ["马尔可夫决策过程", "状态", "动作", "奖励"],
        "keep_english": [],
        "description": "测试 MDP 相关术语"
    },
    {
        "text": "Large language models like GPT can perform various NLP tasks.",
        "expected_terms": ["大语言模型", "GPT", "NLP"],
        "keep_english": ["GPT", "NLP"],  # 缩写保持英文
        "description": "测试混合术语 (缩写保持英文)"
    }
]

# ==================== 主程序 ====================

def get_first_glossary():
    """自动获取第一个可用的术语表"""
    url = f"{API_BASE_URL}/v2/glossaries"
    headers = {"Authorization": f"DeepL-Auth-Key {API_KEY}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        glossaries = response.json().get("glossaries", [])

        if not glossaries:
            print("❌ 错误: 没有找到任何术语表!")
            print("请先运行 create_deepl_glossary.py 创建术语表")
            return None

        glossary = glossaries[0]
        print(f"\n📋 使用术语表:")
        print(f"名称: {glossary['name']}")
        print(f"ID: {glossary['glossary_id']}")
        print(f"语言对: {glossary['source_lang']} → {glossary['target_lang']}")
        print(f"术语数量: {glossary['entry_count']}")
        print("=" * 60)

        return glossary['glossary_id']

    except Exception as e:
        print(f"❌ 获取术语表失败: {e}")
        return None


def translate_text(text, use_glossary=True, glossary_id=None):
    """翻译文本，可选择是否使用术语表"""
    url = f"{API_BASE_URL}/v2/translate"
    headers = {
        "Authorization": f"DeepL-Auth-Key {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "text": [text],
        "source_lang": "EN",
        "target_lang": "ZH"
    }

    # 如果使用术语表，添加 glossary_id
    if use_glossary and glossary_id:
        payload["glossary_id"] = glossary_id

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        result = response.json()
        return result["translations"][0]["text"]

    except Exception as e:
        print(f"❌ 翻译失败: {e}")
        return None


def highlight_terms(text, terms):
    """高亮显示文本中的术语（简单版）"""
    highlighted = text
    for term in terms:
        if term in text:
            highlighted = highlighted.replace(term, f"【{term}】")
    return highlighted


def run_tests():
    """运行所有测试用例"""

    # 获取 Glossary ID
    global GLOSSARY_ID
    if not GLOSSARY_ID:
        GLOSSARY_ID = get_first_glossary()
        if not GLOSSARY_ID:
            return

    print("\n" + "=" * 60)
    print("开始测试术语表翻译 (每个测试都会对比使用/不使用术语表)")
    print("=" * 60)

    passed = 0
    failed = 0
    comparison_results = []  # 存储对比结果

    for i, test_case in enumerate(TEST_CASES, 1):
        print(f"\n{'='*60}")
        print(f"[测试 {i}/{len(TEST_CASES)}] {test_case['description']}")
        print("=" * 60)
        print(f"📝 原文: {test_case['text']}")
        print("-" * 60)

        # 1️⃣ 不使用术语表翻译
        print(f"\n[1] 🚫 不使用术语表翻译:")
        translation_without_glossary = translate_text(
            test_case['text'],
            use_glossary=False
        )

        if not translation_without_glossary:
            print("❌ 翻译失败")
        else:
            print(f"    {translation_without_glossary}")

        # 2️⃣ 使用术语表翻译
        print(f"\n[2] ✅ 使用术语表翻译:")
        translation_with_glossary = translate_text(
            test_case['text'],
            use_glossary=True,
            glossary_id=GLOSSARY_ID
        )

        if not translation_with_glossary:
            print("❌ 翻译失败，跳过")
            failed += 1
            continue
        else:
            print(f"    {translation_with_glossary}")

        # 3️⃣ 差异分析
        print(f"\n[3] 🔍 差异分析:")

        if translation_without_glossary == translation_with_glossary:
            print("    ⚠️  两次翻译结果相同，术语表可能未对此文本生效")
            has_difference = False
        else:
            print("    ✅ 两次翻译结果不同，术语表已生效!")
            has_difference = True

            # 找出具体差异
            words_without = translation_without_glossary.split()
            words_with = translation_with_glossary.split()

            print(f"\n    差异部分:")
            print(f"    不使用术语表: {translation_without_glossary}")
            print(f"    使用术语表:   {translation_with_glossary}")

        # 4️⃣ 检查期望的术语是否出现
        print(f"\n[4] 📊 术语检测:")
        found_terms = []
        missing_terms = []
        keep_english_terms = test_case.get('keep_english', [])

        for term in test_case['expected_terms']:
            if term in translation_with_glossary:
                found_terms.append(term)
                # 判断是"保持英文"还是"翻译为中文"
                is_keep_english = term in keep_english_terms

                if translation_without_glossary:
                    if term not in translation_without_glossary:
                        if is_keep_english:
                            print(f"    ✅ 【{term}】- 保持英文成功 (原翻译会被翻译)")
                        else:
                            print(f"    ✅ 【{term}】- 术语表翻译生效 (原翻译不同)")
                    else:
                        if is_keep_english:
                            print(f"    ℹ️  【{term}】- 保持英文 (DeepL默认也保持)")
                        else:
                            print(f"    ℹ️  【{term}】- 已存在 (无需术语表也能正确翻译)")
                else:
                    if is_keep_english:
                        print(f"    ✅ 【{term}】- 保持英文")
                    else:
                        print(f"    ✅ 【{term}】- 找到")
            else:
                missing_terms.append(term)
                is_keep_english = term in keep_english_terms
                if is_keep_english:
                    print(f"    ❌ 【{term}】- 未能保持英文 (可能被翻译了)")
                else:
                    print(f"    ❌ 【{term}】- 未找到")

        # 显示统计
        print(f"\n    术语匹配: {len(found_terms)}/{len(test_case['expected_terms'])}")
        if keep_english_terms:
            keep_english_found = [t for t in found_terms if t in keep_english_terms]
            print(f"    保持英文: {len(keep_english_found)}/{len(keep_english_terms)}")

        # 5️⃣ 高亮显示
        print(f"\n[5] 🎨 术语高亮显示:")
        if found_terms:
            highlighted = highlight_terms(translation_with_glossary, found_terms)
            print(f"    {highlighted}")
        else:
            print(f"    {translation_with_glossary} (无术语)")

        # 6️⃣ 判断测试结果
        print(f"\n[6] 📝 测试结果:")
        test_passed = len(found_terms) == len(test_case['expected_terms'])

        if test_passed and has_difference:
            print("    ✅ 完全通过! (所有术语都匹配，且术语表生效)")
            passed += 1
            result_status = "完全通过"
        elif test_passed and not has_difference:
            print("    ⚠️  术语匹配但无差异 (术语表可能未起作用)")
            result_status = "术语匹配但无差异"
        elif len(found_terms) > 0:
            print(f"    ⚠️  部分通过 (找到 {len(found_terms)}/{len(test_case['expected_terms'])} 个术语)")
            failed += 1
            result_status = "部分通过"
        else:
            print("    ❌ 失败 (未找到任何期望术语)")
            failed += 1
            result_status = "失败"

        # 记录对比结果
        comparison_results.append({
            "test_num": i,
            "description": test_case['description'],
            "original": test_case['text'],
            "without_glossary": translation_without_glossary,
            "with_glossary": translation_with_glossary,
            "found_terms": found_terms,
            "missing_terms": missing_terms,
            "has_difference": has_difference,
            "status": result_status
        })

        print("-" * 60)

    # 总结报告
    print("\n" + "=" * 60)
    print("📊 详细对比总结")
    print("=" * 60)

    for result in comparison_results:
        print(f"\n[测试 {result['test_num']}] {result['description']} - {result['status']}")
        print(f"原文: {result['original'][:50]}...")
        print(f"不使用术语表: {result['without_glossary']}")
        print(f"使用术语表:   {result['with_glossary']}")
        if result['has_difference']:
            print(f"✅ 术语表生效: {', '.join(['【' + t + '】' for t in result['found_terms']])}")
        else:
            print(f"⚠️  无明显差异")
        print("-" * 60)

    # 最终统计
    print("\n" + "=" * 60)
    print("🎯 最终测试统计")
    print("=" * 60)
    print(f"✅ 完全通过: {passed}/{len(TEST_CASES)}")
    print(f"⚠️  失败/部分: {failed}/{len(TEST_CASES)}")
    print(f"📈 通过率: {passed/len(TEST_CASES)*100:.1f}%")

    # 术语表效果统计
    effective_count = sum(1 for r in comparison_results if r['has_difference'])
    print(f"🔄 术语表生效次数: {effective_count}/{len(TEST_CASES)}")
    print(f"📊 术语表生效率: {effective_count/len(TEST_CASES)*100:.1f}%")

    if passed == len(TEST_CASES):
        print("\n🎉 所有测试通过! 术语表工作正常!")
    elif passed > 0:
        print("\n⚠️  部分测试通过，请检查术语表内容")
    else:
        print("\n❌ 所有测试失败，请检查:")
        print("1. 术语表是否正确创建")
        print("2. Glossary ID 是否正确")
        print("3. API Key 是否有效")


def interactive_test():
    """交互式测试模式"""

    # 获取 Glossary ID
    global GLOSSARY_ID
    if not GLOSSARY_ID:
        GLOSSARY_ID = get_first_glossary()
        if not GLOSSARY_ID:
            return

    print("\n" + "=" * 60)
    print("交互式对比测试模式")
    print("=" * 60)
    print("输入英文文本，程序会对比使用/不使用术语表的翻译结果")
    print("输入 'quit' 退出")
    print("=" * 60)

    while True:
        text = input("\n📝 请输入英文文本: ").strip()

        if text.lower() == 'quit':
            print("👋 再见!")
            break

        if not text:
            continue

        print("\n" + "=" * 60)
        print(f"原文: {text}")
        print("=" * 60)

        # 1. 不使用术语表
        print("\n[1] 🚫 不使用术语表:")
        trans1 = translate_text(text, use_glossary=False)
        if trans1:
            print(f"    译文: {trans1}")
        else:
            print("    ❌ 翻译失败")

        # 2. 使用术语表
        print("\n[2] ✅ 使用术语表:")
        trans2 = translate_text(text, use_glossary=True, glossary_id=GLOSSARY_ID)
        if trans2:
            print(f"    译文: {trans2}")
        else:
            print("    ❌ 翻译失败")

        # 3. 对比分析
        if trans1 and trans2:
            print("\n[3] 🔍 对比分析:")
            if trans1 != trans2:
                print("    ✅ 术语表生效! 翻译结果不同")

                # 高亮显示差异
                print(f"\n    不使用术语表: {trans1}")
                print(f"    使用术语表:   {trans2}")

                # 尝试找出可能的术语替换
                words1 = set(trans1.split())
                words2 = set(trans2.split())

                only_in_glossary = words2 - words1
                only_in_normal = words1 - words2

                if only_in_glossary or only_in_normal:
                    print(f"\n    可能被术语表替换的词:")
                    if only_in_normal:
                        print(f"    原翻译: {', '.join(only_in_normal)}")
                    if only_in_glossary:
                        print(f"    术语表: {', '.join(only_in_glossary)}")
            else:
                print("    ⚠️  两次翻译结果相同")
                print("    可能原因:")
                print("    - 文本中没有包含术语表中的术语")
                print("    - DeepL 默认翻译已经符合术语表定义")

        print("-" * 60)


if __name__ == "__main__":
    import sys

    print("=" * 60)
    print("DeepL Glossary 测试工具")
    print("=" * 60)
    print("\n选择测试模式:")
    print("1. 自动测试 (运行预设测试用例)")
    print("2. 交互测试 (手动输入文本)")
    print("0. 退出")

    choice = input("\n请选择 (0-2): ").strip()

    if choice == "1":
        run_tests()
    elif choice == "2":
        interactive_test()
    elif choice == "0":
        print("👋 再见!")
    else:
        print("❌ 无效选项")

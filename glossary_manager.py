#!/usr/bin/env python3
"""
DeepL Glossary Manager
A tool to create and manage glossaries for DeepL API,
designed for academic research and literature translation.

Author: wzhxzkk
License: MIT
Repository: https://github.com/wzhxzkk/deepl-glossary-manager
"""

import requests
import json
import sys
import os
from pathlib import Path

# ==================== Configuration ====================

# Your DeepL API Key
# For Free API: Get from https://www.deepl.com/pro-api (ends with ':fx')
# For Pro API: Get from your DeepL account
API_KEY = os.environ["API_KEY"]

# API Endpoint
# Free API users: "https://api-free.deepl.com"
# Pro/Team users: "https://api.deepl.com"
API_BASE_URL = "https://api-free.deepl.com"

# Glossary Name
GLOSSARY_NAME = "Academic_AI_Terms"

# Source and Target Languages
SOURCE_LANG = "en"  # English
TARGET_LANG = "zh"  # Chinese

# ==================== Terms Configuration ====================
# Format: "English term": "Chinese translation" or "English term": "English term" (to keep English)
#
# Two types of terms:
# 1. Keep English: "LLM": "LLM"
# 2. Translate to Chinese: "policy": "策略"

TERMS = {
    # ========== Keep English (Abbreviations and Proper Nouns) ==========
    "LLM": "LLM",
    "LLMs": "LLM",
    "GPT": "GPT",
    "API": "API",
    "NLP": "NLP",

    # ========== Translate to Chinese (Full Terms) ==========
    "large language model": "大语言模型",
    "large language models": "大语言模型",
    "reinforcement learning": "强化学习",
    "embodied AI": "具身智能",
    "embodied decision making": "具身决策",
    "policy": "策略",
    "reward": "奖励",
    "agent": "agent",  # Keep English or change to "智能体"
    "environment": "环境",
    "state": "状态",
    "action": "动作",
    "Markov Decision Process": "马尔可夫决策过程",
    "MDP": "马尔可夫决策过程",
    "Q-learning": "Q学习",
    "actor-critic": "演员-评论家",
    "imitation learning": "模仿学习",
    "demonstration": "演示",
    "trajectory": "轨迹",
    "visuomotor control": "视觉-运动控制",
    "multimodal": "多模态",
}

# ==================== Main Functions ====================

def create_glossary():
    """Create a new DeepL Glossary"""

    # Build TSV format entries
    entries = "\n".join([f"{en}\t{zh}" for en, zh in TERMS.items()])

    print("=" * 60)
    print("DeepL Glossary Creation Tool")
    print("=" * 60)
    print(f"\n📝 Glossary Name: {GLOSSARY_NAME}")
    print(f"🌐 Language Pair: {SOURCE_LANG} → {TARGET_LANG}")
    print(f"📊 Number of Terms: {len(TERMS)}")
    print(f"\nTerms Preview:")
    print("-" * 60)
    for i, (en, zh) in enumerate(list(TERMS.items())[:5], 1):
        print(f"{i}. {en} → {zh}")
    if len(TERMS) > 5:
        print(f"... and {len(TERMS) - 5} more terms")
    print("-" * 60)

    # Send creation request
    url = f"{API_BASE_URL}/v2/glossaries"
    headers = {
        "Authorization": f"DeepL-Auth-Key {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "name": GLOSSARY_NAME,
        "source_lang": SOURCE_LANG,
        "target_lang": TARGET_LANG,
        "entries": entries,
        "entries_format": "tsv"
    }

    print(f"\n🚀 Creating glossary...")

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        result = response.json()
        glossary_id = result["glossary_id"]

        print("\n✅ Glossary created successfully!")
        print("=" * 60)
        print(f"Glossary ID: {glossary_id}")
        print(f"Created: {result['creation_time']}")
        print(f"Entry Count: {result['entry_count']}")
        print("=" * 60)

        # Generate plugin secret format
        plugin_secret = f"{API_KEY}#{glossary_id}"

        print(f"\n📋 Copy this complete key to your Zotero plugin settings:")
        print("-" * 60)
        print(plugin_secret)
        print("-" * 60)

        print(f"\n💡 Usage Instructions:")
        print(f"1. Open Zotero -> Tools -> Translate for Zotero -> Preferences")
        print(f"2. Find 'DeepL Free' service")
        print(f"3. Paste the complete key above into the key input box")
        print(f"4. Your glossary will now be used automatically!")

        # Save to file
        output_file = Path("deepl_glossary_info.txt")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"Glossary ID: {glossary_id}\n")
            f.write(f"Plugin Secret: {plugin_secret}\n")
            f.write(f"\nCreated: {result['creation_time']}\n")
            f.write(f"Entry Count: {result['entry_count']}\n")

        print(f"\n💾 Glossary info saved to: {output_file}")

    except requests.exceptions.HTTPError as e:
        print(f"\n❌ Error: {e}")
        print(f"Response: {e.response.text}")
        print(f"\nPossible causes:")
        print(f"- Incorrect API Key")
        print(f"- Wrong API endpoint (Free vs Pro)")
        print(f"- Network connection issue")
        print(f"- Already have maximum glossaries (Free API: 1 glossary)")
    except Exception as e:
        print(f"\n❌ Unknown error: {e}")


def list_glossaries():
    """List all created glossaries"""
    url = f"{API_BASE_URL}/v2/glossaries"
    headers = {"Authorization": f"DeepL-Auth-Key {API_KEY}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        glossaries = response.json().get("glossaries", [])

        if not glossaries:
            print("\n📋 No glossaries found")
            return glossaries

        print(f"\n📋 Existing Glossaries ({len(glossaries)}):")
        print("=" * 60)
        for i, g in enumerate(glossaries, 1):
            print(f"\n[{i}] Name: {g['name']}")
            print(f"    ID: {g['glossary_id']}")
            print(f"    Languages: {g['source_lang']} → {g['target_lang']}")
            print(f"    Entries: {g['entry_count']}")
            print(f"    Created: {g['creation_time']}")
            print(f"\n    Plugin Key: {API_KEY}#{g['glossary_id']}")
            print("-" * 60)

        return glossaries

    except Exception as e:
        print(f"\n❌ Error: {e}")
        return []


def get_glossary_entries(glossary_id):
    """Get detailed contents of a glossary"""
    url = f"{API_BASE_URL}/v2/glossaries/{glossary_id}/entries"
    headers = {"Authorization": f"DeepL-Auth-Key {API_KEY}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # DeepL returns TSV format
        tsv_content = response.text

        print(f"\n📖 Glossary Contents:")
        print("=" * 60)

        entries = []
        for line in tsv_content.strip().split('\n'):
            if '\t' in line:
                source, target = line.split('\t', 1)
                entries.append((source, target))
                print(f"{source} → {target}")

        print("=" * 60)
        print(f"Total: {len(entries)} terms")

        return entries

    except Exception as e:
        print(f"\n❌ Error: {e}")
        return []


def delete_glossary(glossary_id):
    """Delete a specific glossary"""
    url = f"{API_BASE_URL}/v2/glossaries/{glossary_id}"
    headers = {"Authorization": f"DeepL-Auth-Key {API_KEY}"}

    try:
        # Get glossary info first
        info_response = requests.get(url, headers=headers)
        if info_response.status_code == 200:
            info = info_response.json()
            print(f"\n⚠️  About to delete glossary:")
            print(f"Name: {info['name']}")
            print(f"ID: {info['glossary_id']}")
            print(f"Languages: {info['source_lang']} → {info['target_lang']}")
            print(f"Entries: {info['entry_count']}")

            confirm = input(f"\nConfirm deletion? (yes/no): ").strip().lower()
            if confirm != 'yes':
                print("❌ Deletion cancelled")
                return False

        # Execute deletion
        response = requests.delete(url, headers=headers)

        if response.status_code == 204:
            print("\n✅ Glossary deleted successfully!")
            return True
        else:
            print(f"\n❌ Deletion failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False

    except Exception as e:
        print(f"\n❌ Error: {e}")
        return False


def delete_all_glossaries():
    """Delete all glossaries"""
    glossaries = list_glossaries()

    if not glossaries:
        return

    print(f"\n⚠️  About to delete all {len(glossaries)} glossaries!")
    confirm = input(f"\nConfirm delete all glossaries? (yes/no): ").strip().lower()

    if confirm != 'yes':
        print("❌ Deletion cancelled")
        return

    success_count = 0
    for g in glossaries:
        url = f"{API_BASE_URL}/v2/glossaries/{g['glossary_id']}"
        headers = {"Authorization": f"DeepL-Auth-Key {API_KEY}"}

        try:
            response = requests.delete(url, headers=headers)
            if response.status_code == 204:
                print(f"✅ Deleted: {g['name']} ({g['glossary_id']})")
                success_count += 1
            else:
                print(f"❌ Failed to delete: {g['name']}")
        except Exception as e:
            print(f"❌ Error deleting {g['name']}: {e}")

    print(f"\n✅ Successfully deleted {success_count}/{len(glossaries)} glossaries")


def update_glossary():
    """Update glossary (delete old and create new)

    Note: DeepL Free API only allows 1 glossary
    To modify terms, you must delete the old one and create a new one
    """
    print("\n" + "=" * 60)
    print("⚠️  DeepL Free API Limitation")
    print("=" * 60)
    print("DeepL Free API only allows 1 glossary")
    print("Updating requires:")
    print("1. Delete existing glossary")
    print("2. Create new glossary with updated terms")
    print("=" * 60)

    # Check existing glossaries
    glossaries = list_glossaries()

    if not glossaries:
        print("\n✅ No existing glossary, can create new one directly")
        confirm = input("\nCreate new glossary? (yes/no): ").strip().lower()
        if confirm == 'yes':
            create_glossary()
        return

    if len(glossaries) > 1:
        print(f"\n⚠️  Warning: Detected {len(glossaries)} glossaries")
        print("This shouldn't happen with Free API")

    # Show current terms
    print("\n📖 Current glossary contents:")
    current_entries = get_glossary_entries(glossaries[0]['glossary_id'])

    print(f"\n📝 Will replace with new terms:")
    print("-" * 60)
    for i, (en, zh) in enumerate(list(TERMS.items())[:5], 1):
        print(f"{i}. {en} → {zh}")
    if len(TERMS) > 5:
        print(f"... and {len(TERMS) - 5} more terms")
    print("-" * 60)
    print(f"Total: {len(TERMS)} new terms")

    # Confirm update
    confirm = input("\n⚠️  Confirm delete old glossary and create new one? (yes/no): ").strip().lower()

    if confirm != 'yes':
        print("❌ Update cancelled")
        return

    # Delete old glossary
    print("\n🗑️  Deleting old glossary...")
    url = f"{API_BASE_URL}/v2/glossaries/{glossaries[0]['glossary_id']}"
    headers = {"Authorization": f"DeepL-Auth-Key {API_KEY}"}

    try:
        response = requests.delete(url, headers=headers)
        if response.status_code == 204:
            print("✅ Old glossary deleted")
        else:
            print(f"❌ Deletion failed: {response.status_code}")
            return
    except Exception as e:
        print(f"❌ Deletion failed: {e}")
        return

    # Create new glossary
    print("\n🚀 Creating new glossary...")
    create_glossary()


def main():
    """Main function"""

    if API_KEY == "YOUR_DEEPL_API_KEY_HERE":
        print("❌ Please set your DeepL API Key first!")
        print("Edit the API_KEY variable in this script")
        sys.exit(1)

    while True:
        print("\n" + "=" * 60)
        print("DeepL Glossary Manager")
        print("=" * 60)
        print("\n⚠️  Note: DeepL Free API only allows 1 glossary")
        print("\nSelect an option:")
        print("1. Create new glossary")
        print("2. List all glossaries")
        print("3. View glossary contents")
        print("4. Delete specific glossary")
        print("5. Delete all glossaries")
        print("6. Update glossary (recommended)")
        print("0. Exit")

        choice = input("\nEnter option (0-6): ").strip()

        if choice == "0":
            print("\n👋 Goodbye!")
            break
        elif choice == "1":
            create_glossary()
        elif choice == "2":
            list_glossaries()
        elif choice == "3":
            glossaries = list_glossaries()
            if glossaries:
                glossary_id = input("\nEnter glossary ID (or press Enter to return): ").strip()
                if glossary_id:
                    get_glossary_entries(glossary_id)
        elif choice == "4":
            glossaries = list_glossaries()
            if glossaries:
                glossary_id = input("\nEnter glossary ID to delete (or press Enter to return): ").strip()
                if glossary_id:
                    delete_glossary(glossary_id)
        elif choice == "5":
            delete_all_glossaries()
        elif choice == "6":
            update_glossary()
        else:
            print("❌ Invalid option, please try again")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()

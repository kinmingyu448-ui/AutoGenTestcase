# 创建 cli_claude.py
import anthropic
import sys

client = anthropic.Anthropic(api_key="your-key")

print("Claude 终端助手 (输入 'quit' 退出)")
while True:
    user_input = input("\n你: ")
    if user_input.lower() in ['quit', 'exit', 'q']:
        break

    response = client.messages.create(
        model="claude-3-haiku-20240307",  # 使用更快的模型
        max_tokens=500,
        messages=[{"role": "user", "content": user_input}]
    )
    print(f"\nClaude: {response.content[0].text}")
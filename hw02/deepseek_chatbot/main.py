from openai import OpenAI
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()

def get_deepseek_client():
    """创建并返回 DeepSeek 客户端"""
    return OpenAI(
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        base_url="https://api.deepseek.com"
    )

def chat_with_deepseek(user_question):
    """
    调用 DeepSeek 模型获取回答
    :param user_question: 用户问题
    :return: 模型回复
    """
    client = get_deepseek_client()
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": user_question}],
        stream=False
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("=" * 50)
    print("💬 DeepSeek 聊天机器人已启动（输入 exit 退出）")
    print("=" * 50)

    while True:
        user_input = input("\n你：")
        if user_input.strip().lower() in ["exit", "quit", "q"]:
            print("\n👋 再见！")
            break
        
        try:
            reply = chat_with_deepseek(user_input)
            print(f"\nAI：{reply}")
        except Exception as e:
            print(f"\n❌ 出错了：{str(e)}")
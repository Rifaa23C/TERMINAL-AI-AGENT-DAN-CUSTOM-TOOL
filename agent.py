import json
import requests
from colorama import init, Fore, Style
init(autoreset=True)

from tools import tool_dictionary
from tool_schema import tool_schema

# Catatan:
# API key saya tidak saya tulis di sini untuk alasan keamanan.
# Program akan mengambil API dari environment variable OPENROUTER_API_KEY.
import os
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

class LLM_API_AGENT:
    def __init__(self):
        self.model = "x-ai/grok-4-fast"
        self.headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }
        self.payload = {
            "model": self.model,
            "messages": [],
            "tools": tool_schema,
            "tool_choice": "auto",
            "stream": True
        }

    def set_system_prompt(self, system_prompt: str):
        self.payload["messages"].append(
            {"role": "system", "content": system_prompt}
        )

    def add_message(self, role: str, content: str):
        self.payload["messages"].append(
            {"role": role, "content": content}
        )

    def add_tool_call(self, tool_call_id: str, tool_call_response: str):
        self.payload["messages"].append({
            "role": "tool",
            "content": tool_call_response,
            "tool_call_id": tool_call_id
        })

    def get_response(self):
        response_text = ""
        tool_calls = []

        response = requests.post(
            f"{OPENROUTER_BASE_URL}/chat/completions",
            headers=self.headers,
            json=self.payload,
            stream=True
        )

        response.raise_for_status()

        for chunk in response.iter_lines():
            if chunk:
                data = chunk.decode("utf-8")
                if data.startswith("data: "):
                    data = data[6:]

                    if data.strip() == "[DONE]":
                        break

                    data = json.loads(data)
                    delta = data["choices"][0]["delta"]

                    #STREAM OUTPUT (Cyan)
                    if delta.get("content"):
                        print(Fore.CYAN + delta["content"], end="", flush=True)
                        response_text += delta["content"]

                    #TOOL CALL (Thinking = Kuning)
                    if delta.get("tool_calls"):
                        for tool in delta["tool_calls"]:
                            args = json.loads(tool["function"]["arguments"])
                            tool_calls.append({
                                "tool_call_id": tool["id"],
                                "name": tool["function"]["name"],
                                "arguments": args
                            })

        print("\n")
        return response_text, tool_calls

# MAIN PROGRAM
agent = LLM_API_AGENT()

agent.set_system_prompt(
    "You are a helpful assistant. "
    "You can call tools to answer questions. "
    "Return structured results in markdown when useful."
)


while True:
    response, tool_calls = agent.get_response()

    if len(tool_calls) > 0:

        print(Fore.YELLOW + "\nAI is calling tools:", tool_calls, "\n" + Style.RESET_ALL)

        for tool in tool_calls:
            name = tool["name"]
            args = tool["arguments"]

            # menjalankan function di tools.py
            result = tool_dictionary[name](**args)
            print(Fore.YELLOW + "Tool Execution Result:", result)

            # mengirim hasil tool balik ke LLM
            agent.add_tool_call(
                tool["tool_call_id"],
                json.dumps(result)
            )

        print("\n")

    else:

        # User Input (Hijau)
        user_input = input(Fore.GREEN + "You: " + Style.RESET_ALL)

        if user_input.lower() in ["quit", "exit", "q"]:
            break

        agent.add_message("user", user_input)


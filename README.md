# Fifa2026-Pred

Main files and start
- Main-Analysis.ipynb: Entry point, includes all relevant games metadata LLM-prompts of every Agent.
- predictions_ledger: The central ledger with commit full history (including bookmakers data) for every game-prediction  in this prospective live study (max. 24 h before official game started).

The DAG-based implementantion uses 4 Agents to predict a football game, using Google GenAI package to access Gemini 3.1. Pro.
All LLM calls are executed via the method ask_agent_with_search(prompt) in in subfolder DIC_LLM
You have to use and load your own API key from your OS environment or use another wrapper than the DIC_LLM/ask_agent_with_search method. In this code the key is loaded via api_key = os.environ.get("GEMINI_API_KEY") in DIC_LLM agent_module.py
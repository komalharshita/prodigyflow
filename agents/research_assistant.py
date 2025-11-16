from typing import List, Dict


class StubWebSearchTool:
def search(self, query: str, top_k: int = 5) -> List[Dict]:
# Returns deterministic stub results to make demos reproducible
return [
{"title": f"{query} - Intro {i}", "url": f"https://example.com/{query.replace(' ','_')}/{i}", "snippet": f"Snippet for {query} (result {i})"}
for i in range(1, top_k+1)
]




class ResearchAssistantAgent:
def __init__(self, search_tool=None, memory=None):
self.search_tool = search_tool or StubWebSearchTool()
self.memory = memory


def fetch_resources(self, topic: str, top_k: int = 5) -> List[Dict]:
query = f"{topic} tutorial"
results = self.search_tool.search(query, top_k=top_k)
# Simple ranking: keep as-is. Real implementation would apply heuristics
bundle = []
for r in results:
bundle.append({
"title": r["title"],
"url": r["url"],
"snippet": r["snippet"]
})
if self.memory:
self.memory.set("global", f"last_resources:{topic}", bundle)
return bundle

from typing import Dict, Any


class StubCodeExecTool:
def execute(self, code: str, lang: str = "python") -> Dict[str, Any]:
# WARNING: This is a stub and DOES NOT execute untrusted code.
# In production you must sandbox and limit resources.
try:
# For safety, we won't execute arbitrary code here. Return a stubbed response.
return {"stdout": "(execution disabled)", "stderr": "", "exit_code": 0}
except Exception as e:
return {"stdout": "", "stderr": str(e), "exit_code": 1}




class DoubtSolverAgent:
def __init__(self, llm_client=None, code_exec_tool=None, memory=None):
self.llm = llm_client
self.code_exec = code_exec_tool or StubCodeExecTool()
self.memory = memory


def summarize(self, resource: Dict) -> str:
# resource: {"title","url","snippet"}
snippet = resource.get("snippet", "")
# Use a simple heuristic summary for a demo
return f"Summary: {snippet[:200]}"


def explain_concept(self, concept: str, level: str = "intro") -> str:
# level can be 'intro', 'intermediate', 'detailed'
return f"Explanation of {concept} (level={level}). Example and steps would go here."


def run_code(self, code: str, lang: str = "python") -> Dict[str, Any]:
return self.code_exec.execute(code, lang=lang)


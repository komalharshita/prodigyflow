from core.orchestrator import Orchestrator
from rich import print

def main():
    print("[bold cyan]Welcome to ProdigyFlow![/bold cyan]")
    orchestrator = Orchestrator()

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ["exit", "quit"]:
            print("[bold red]Exiting ProdigyFlow...[/bold red]")
            break

        response = orchestrator.route(user_input)
        print("\n[green]Agent Response:[/green]")
        print(response)

if __name__ == "__main__":
    main()

from agents.loop_agent import LoopAgent

loop = LoopAgent()
print("Loop Agent Demo:")
print(loop.run_until_complete("Review topic", steps=3))

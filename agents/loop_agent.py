import logging

class LoopAgent:
    def run_until_complete(self, task, steps=3):
        logs = []
        for i in range(steps):
            step_log = f"Step {i+1}: {task} completed."
            logging.info(step_log)
            logs.append(step_log)
        return logs

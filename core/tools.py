import logging
logging.basicConfig(level=logging.INFO)


def estimate_time(total_hours, num_topics):
    if num_topics == 0:
        return total_hours
    return total_hours / num_topics

# Simple agent output evaluator
def evaluate_output(output):
    score = "good" if len(str(output)) > 30 else "needs improvement"
    return {"evaluation": score, "length": len(str(output))}

# Mock A2A Protocol
class A2AProtocol:
    def send(self, sender, receiver, message):
        return {
            "from": sender,
            "to": receiver,
            "message": message
        }


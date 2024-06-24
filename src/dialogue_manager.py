
from ..os_copilot import FridayAgent, ToolManager, FridayExecutor, FridayPlanner, FridayRetriever
from ..os_copilot.utils import setup_config, setup_pre_run

class DialogueManager:
    def __init__(self, client):
        self.client = client
        self.messages = []

    def check_intent_and_execute(self, transcript):
        args = setup_config()
        if not args.query:
            args.query = transcript['text']
        
        task = setup_pre_run(args)
        agent = FridayAgent(FridayPlanner, FridayRetriever, FridayExecutor, ToolManager, config=args)
        result = agent.run(task=task)
        return result

    def handle_dialogue(self, transcript):
        self.messages.append({
            'role': 'user',
            'content': transcript,
        })

        response = self.client.chat(model='llama3', messages=self.messages)
        self.messages.append({
            'role': 'assistant',
            'content': response['message']['content'],
        })

        if 'bye' in transcript.lower():
            exit()
        
        if "friday" in transcript.lower():
            print("Start planning task...")
            task_result = self.check_intent_and_execute(transcript)
            print("Task result:", task_result)
            # You might want to add the task_result to messages or process it further.
        
        return response['message']['content']
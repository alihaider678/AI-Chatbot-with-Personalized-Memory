import unittest
from chatbot.memory import store_conversation, retrieve_memory
from chatbot.gemini_ai import get_gemini_response

class TestChatbot(unittest.TestCase):
    
    def test_memory_retrieval(self):
        store_conversation("I am going to drink water.")
        response = retrieve_memory("When did I last drink water?")
        self.assertIn("drink water", response)

    def test_gemini_response(self):
        response = get_gemini_response("When did I last drink water?", memory="You mentioned drinking water 5 minutes ago.")
        self.assertNotIn("I don't have any record", response)  

if __name__ == '__main__':
    unittest.main()

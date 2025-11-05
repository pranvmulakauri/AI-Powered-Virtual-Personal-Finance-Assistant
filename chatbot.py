from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

# Download required NLTK data (run once)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')


class FinanceChatbot:
    def __init__(self):
        self.intents = {
            'budget': ['show', 'my', 'budget', 'how', 'much'],
            'spending': ['how', 'much', 'spent', 'spending', 'expense'],
            'savings': ['savings', 'save', 'save', 'goal'],
            'recommendations': ['recommend', 'suggest', 'advice'],
            'report': ['report', 'summary', 'overview']
        }

    def process_query(self, user_input):
        """Process user query and return response"""
        tokens = word_tokenize(user_input.lower())
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [t for t in tokens if t not in stop_words]

        detected_intent = self.detect_intent(filtered_tokens)
        response = self.generate_response(detected_intent)

        return {
            'user_query': user_input,
            'intent': detected_intent,
            'response': response
        }

    def detect_intent(self, tokens):
        """Detect user intent from tokens"""
        for intent, keywords in self.intents.items():
            if any(token in keywords for token in tokens):
                return intent
        return 'general'

    def generate_response(self, intent):
        """Generate chatbot response"""
        responses = {
            'budget': 'Your current budget allocation is: Needs 50%, Wants 30%, Savings 20%.',
            'spending': 'You can view your spending by category in the analytics section.',
            'savings': 'Keep building your emergency fund of 6 months expenses.',
            'recommendations': 'Consider reducing entertainment spending and increasing savings.',
            'report': 'Your monthly financial report is ready for download.',
            'general': 'I can help you with budgeting, spending analysis, and savings goals.'
        }
        return responses.get(intent, responses['general'])

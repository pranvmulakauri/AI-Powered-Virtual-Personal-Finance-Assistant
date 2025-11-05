from modules.authentication import UserAuthentication
from modules.data_processor import TransactionProcessor
from modules.budget_analyzer import BudgetAnalyzer
from modules.chatbot import FinanceChatbot
from modules.reporting import ReportGenerator
from config import SECRET_KEY, BUDGET_WARNING_THRESHOLD
import pandas as pd



class FinanceAssistant:
    def __init__(self):
        self.auth = UserAuthentication()
        self.processor = TransactionProcessor()
        self.analyzer = BudgetAnalyzer()
        self.chatbot = FinanceChatbot()
        self.reporter = ReportGenerator()
        self.current_user = None

    def start_application(self):
        """Start the finance assistant"""
        print("=" * 50)
        print("Welcome to AI Finance Assistant")
        print("=" * 50)

        while True:
            if self.current_user is None:
                self.authentication_menu()
            else:
                self.main_menu()

    def authentication_menu(self):
        """Handle authentication"""
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            email = input("Enter email: ")
            result = self.auth.register_user(username, password, email)
            print(result['message'])

        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            result = self.auth.login_user(username, password)
            if result['status']:
                self.current_user = username
                print(f"Welcome, {self.current_user}!")
            else:
                print(result['message'])

        elif choice == '3':
            print("Thank you for using Finance Assistant!")
            exit()

    def main_menu(self):
        """Main application menu"""
        print(f"\n{'=' * 50}")
        print(f"Hello, {self.current_user}")
        print(f"{'=' * 50}")
        print("\n1. Add Transaction")
        print("2. View Spending Patterns")
        print("3. Generate Budget")
        print("4. Get Savings Recommendations")
        print("5. Chat with Assistant")
        print("6. Generate Report")
        print("7. Logout")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            self.add_transaction()
        elif choice == '2':
            self.view_spending_patterns()
        elif choice == '3':
            self.generate_budget()
        elif choice == '4':
            self.get_savings_recommendations()
        elif choice == '5':
            self.chat_with_assistant()
        elif choice == '6':
            self.generate_report()
        elif choice == '7':
            self.current_user = None
            print("Logged out successfully!")

    def add_transaction(self):
        """Add a new transaction"""
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")
        transaction = self.processor.add_transaction(amount, description)
        print(f"\nTransaction added: {transaction}")

    def view_spending_patterns(self):
        """Display spending patterns"""
        patterns = self.processor.identify_spending_patterns()
        if patterns:
            print("\nSpending by Category:")
            for category, amount in patterns.items():
                print(f"  {category}: ₹{amount:.2f}")
        else:
            print("No transactions found.")

    def generate_budget(self):
        """Generate monthly budget"""
        income = float(input("Enter your monthly income: "))
        patterns = self.processor.identify_spending_patterns()
        budget = self.analyzer.generate_budget(income, patterns)

        print("\nRecommended Budget:")
        for category, amount in budget.items():
            print(f"  {category}: ₹{amount:.2f}")

    def get_savings_recommendations(self):
        """Get savings recommendations"""
        income = float(input("Enter monthly income: "))
        expenses = self.processor.identify_spending_patterns()
        recommendations = self.analyzer.savings_recommendations(income, expenses, [])

        print("\nSavings Recommendations:")
        print(f"  Monthly Surplus: ₹{recommendations['monthly_surplus']:.2f}")
        print(f"  Investment Potential: ₹{recommendations['investment_potential']:.2f}")

    def chat_with_assistant(self):
        """Interact with the chatbot"""
        query = input("\nAsk me anything about your finances: ")
        response = self.chatbot.process_query(query)
        print(f"\nAssistant: {response['response']}")

    def generate_report(self):
        """Generate financial report"""
        report, filename = self.reporter.generate_monthly_report(
            self.processor.transactions,
            {}
        )
        print(f"\nReport generated: {filename}")
        print(f"Total Transactions: {report['transactions_count']}")


if __name__ == "__main__":
    app = FinanceAssistant()
    app.start_application()

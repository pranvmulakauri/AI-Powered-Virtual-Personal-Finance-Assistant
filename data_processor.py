import pandas as pd
import numpy as np
from datetime import datetime


class TransactionProcessor:
    def __init__(self):
        self.transactions = []
        self.categories = {
            'Food': ['restaurant', 'grocery', 'cafe', 'food'],
            'Transport': ['uber', 'taxi', 'fuel', 'bus', 'metro'],
            'Entertainment': ['movie', 'gaming', 'music', 'netflix'],
            'Utilities': ['electricity', 'water', 'internet', 'phone'],
            'Healthcare': ['pharmacy', 'hospital', 'doctor'],
            'Shopping': ['mall', 'amazon', 'flipkart']
        }

    def categorize_transaction(self, description):
        """Automatically categorize transactions"""
        description_lower = description.lower()
        for category, keywords in self.categories.items():
            if any(keyword in description_lower for keyword in keywords):
                return category
        return 'Others'

    def load_transactions(self, file_path):
        """Load transactions from CSV"""
        df = pd.read_csv(file_path)
        self.transactions = df.to_dict('records')
        return df

    def add_transaction(self, amount, description, date=None):
        """Add new transaction"""
        if date is None:
            date = datetime.now().strftime('%Y-%m-%d')

        transaction = {
            'amount': amount,
            'description': description,
            'category': self.categorize_transaction(description),
            'date': date
        }
        self.transactions.append(transaction)
        return transaction

    def identify_spending_patterns(self):
        """Analyze spending patterns by category"""
        df = pd.DataFrame(self.transactions)
        if df.empty:
            return {}

        spending_by_category = df.groupby('category')['amount'].sum().to_dict()
        return spending_by_category

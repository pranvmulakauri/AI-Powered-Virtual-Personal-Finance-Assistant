from datetime import datetime
import pandas as pd
from modules.data_processor import TransactionProcessor  # Add this if needed


class BudgetAnalyzer:
    def __init__(self):
        self.budgets = {}

    def generate_budget(self, monthly_income, spending_patterns):
        """Generate budget based on historical spending"""
        budget = {}

        # Allocate based on common budget rule (50/30/20)
        needs = monthly_income * 0.5
        wants = monthly_income * 0.3
        savings = monthly_income * 0.2

        budget['Needs'] = needs
        budget['Wants'] = wants
        budget['Savings'] = savings

        return budget

    def check_overspending(self, current_spending, budget, threshold=0.9):
        """Notify if user is nearing budget limit"""
        alerts = []
        for category, amount in current_spending.items():
            if category in budget:
                utilization = amount / budget[category]
                if utilization >= threshold:
                    alerts.append({
                        'category': category,
                        'budget': budget[category],
                        'spent': amount,
                        'utilization': utilization * 100,
                        'status': 'warning' if utilization < 1 else 'exceeded'
                    })
        return alerts

    def savings_recommendations(self, income, expenses, goals):
        """Provide savings recommendations"""
        available_for_savings = income - sum(expenses.values())

        recommendations = {
            'monthly_surplus': available_for_savings,
            'emergency_fund_months': 6,
            'emergency_fund_needed': income * 6,
            'investment_potential': available_for_savings * 0.7
        }
        return recommendations

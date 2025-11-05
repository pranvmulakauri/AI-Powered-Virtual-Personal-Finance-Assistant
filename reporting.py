from datetime import datetime
import pandas as pd


class ReportGenerator:
    def __init__(self):
        self.report_format = ['PDF', 'Excel']

    def generate_monthly_report(self, transactions, budget, filename=None):
        """Generate monthly financial health report"""
        if filename is None:
            filename = f"report_{datetime.now().strftime('%Y_%m_%d')}"

        df = pd.DataFrame(transactions)

        report = {
            'generated_at': datetime.now().isoformat(),
            'total_income': df[df['amount'] > 0]['amount'].sum() if 'amount' in df.columns else 0,
            'total_expenses': df[df['amount'] < 0]['amount'].sum() if 'amount' in df.columns else 0,
            'budget_status': budget,
            'transactions_count': len(df)
        }

        return report, filename

    def export_to_excel(self, data, filename):
        """Export report to Excel"""
        df = pd.DataFrame(data)
        excel_file = f"{filename}.xlsx"
        df.to_excel(excel_file, index=False)
        return excel_file

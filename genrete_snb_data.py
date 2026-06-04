import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)
random.seed(42)

#  Settings 
NUM_CUSTOMERS = 5000
START_DATE = datetime(2024, 1, 1)
END_DATE   = datetime(2024, 12, 31)

#  Customer Data 
regions    = ['Riyadh', 'Jeddah', 'Dammam', 'Makkah', 'Madinah', 'Abha', 'Tabuk']
segments   = ['Individual', 'Small Business', 'Medium Business']
products   = ['Credit Card', 'Personal Loan', 'Mortgage', 'Savings Account', 'Investment']
tx_types   = ['Transfer', 'Withdrawal', 'Deposit', 'Bill Payment', 'Purchase']

customers = pd.DataFrame({
    'customer_id':  [f'SNB{str(i).zfill(5)}' for i in range(1, NUM_CUSTOMERS+1)],
    'region':       np.random.choice(regions, NUM_CUSTOMERS, p=[0.35,0.25,0.15,0.10,0.07,0.04,0.04]),
    'segment':      np.random.choice(segments, NUM_CUSTOMERS, p=[0.75,0.15,0.10]),
    'join_date':    [START_DATE - timedelta(days=random.randint(0, 365*3)) for _ in range(NUM_CUSTOMERS)],
    'age':          np.random.randint(18, 70, NUM_CUSTOMERS),
    'credit_score': np.random.randint(300, 900, NUM_CUSTOMERS),
})

#  Transaction Data 
rows = []
for _, cust in customers.iterrows():
    if cust['segment'] == 'Medium Business':
        n_tx = random.randint(20, 60)
    elif cust['segment'] == 'Small Business':
        n_tx = random.randint(10, 30)
    else:
        n_tx = random.randint(1, 20)

    for _ in range(n_tx):
        tx_date = START_DATE + timedelta(days=random.randint(0, 364))

        if cust['segment'] == 'Medium Business':
            amount = round(random.uniform(5000, 200000), 2)
        elif cust['segment'] == 'Small Business':
            amount = round(random.uniform(1000, 50000), 2)
        else:
            amount = round(random.uniform(50, 15000), 2)

        rows.append({
            'transaction_id': f'TX{str(len(rows)).zfill(7)}',
            'customer_id':    cust['customer_id'],
            'date':           tx_date,
            'type':           random.choice(tx_types),
            'amount':         amount,
            'product':        random.choice(products),
        })

transactions = pd.DataFrame(rows)

#  Save Files 
import os
os.makedirs('Data/raw', exist_ok=True)

customers.to_csv('Data/raw/snb_customers.csv', index=False, encoding='utf-8-sig')
transactions.to_csv('Data/raw/snb_transactions.csv', index=False, encoding='utf-8-sig')

print(f'Customers:    {len(customers):,}')
print(f'Transactions: {len(transactions):,}')
print(f'Date range:   {transactions["date"].min().date()} to {transactions["date"].max().date()}')
print(f'\nFiles saved to Data/raw/')

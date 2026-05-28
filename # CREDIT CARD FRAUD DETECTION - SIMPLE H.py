# CREDIT CARD FRAUD DETECTION - SIMPLE HUMAN LOGIC

# -----------------------------------
# STEP 1: SAMPLE TRANSACTION DATA
# -----------------------------------

transactions = [
    {"amount": 500, "time_gap": 30},   # normal
    {"amount": 2000, "time_gap": 5},   # suspicious
    {"amount": 50, "time_gap": 60},    # normal
    {"amount": 5000, "time_gap": 2},   # fraud-like
    {"amount": 1200, "time_gap": 10}   # suspicious
]

# -----------------------------------
# STEP 2: FRAUD DETECTION RULES
# -----------------------------------

def check_fraud(transaction):

    score = 0

    # Rule 1: High amount is risky
    if transaction["amount"] > 1000:
        score += 2
    elif transaction["amount"] > 500:
        score += 1

    # Rule 2: Very fast repeated transaction is risky
    if transaction["time_gap"] < 10:
        score += 2
    elif transaction["time_gap"] < 30:
        score += 1

    # -----------------------------------
    # STEP 3: FINAL DECISION (HUMAN STYLE)
    # -----------------------------------

    if score >= 3:
        return "FRAUD ⚠️"
    else:
        return "LEGIT ✅"


# -----------------------------------
# STEP 4: TEST ALL TRANSACTIONS
# -----------------------------------

for i in transactions:
    result = check_fraud(i)
    print("Transaction:", i, "=>", result)
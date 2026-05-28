# CUSTOMER CHURN PREDICTION - SIMPLE HUMAN LOGIC (NO ML LIBRARIES)

# -----------------------------------
# STEP 1: SAMPLE CUSTOMER DATA
# -----------------------------------

customers = [
    {"name": "Amit", "usage": 80, "complaints": 1, "months": 12},
    {"name": "Ravi", "usage": 20, "complaints": 5, "months": 2},
    {"name": "Sara", "usage": 60, "complaints": 0, "months": 8},
    {"name": "John", "usage": 10, "complaints": 4, "months": 1},
    {"name": "Neha", "usage": 70, "complaints": 2, "months": 10}
]

# -----------------------------------
# STEP 2: CHURN PREDICTION FUNCTION
# -----------------------------------

def predict_churn(customer):

    score = 0

    # Rule 1: Low usage increases churn risk
    if customer["usage"] < 30:
        score += 2
    elif customer["usage"] < 60:
        score += 1

    # Rule 2: More complaints = higher risk
    if customer["complaints"] >= 4:
        score += 2
    elif customer["complaints"] >= 2:
        score += 1

    # Rule 3: New customers are more likely to churn
    if customer["months"] < 3:
        score += 2
    elif customer["months"] < 6:
        score += 1

    # -----------------------------------
    # STEP 3: FINAL DECISION
    # -----------------------------------

    if score >= 4:
        return "CHURN ⚠️"
    else:
        return "NOT CHURNED ✅"


# -----------------------------------
# STEP 4: TEST ALL CUSTOMERS
# -----------------------------------

for c in customers:
    result = predict_churn(c)
    print("Customer:", c["name"], "=>", result)
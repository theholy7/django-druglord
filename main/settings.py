"""
Game related settings

druglord/settings.py is for django related settings
"""

DRUGS = {
    "Coke": {
        "BASE_PRICE": 50,
        "BASE_DANGER": 10,
        "BASE_QUANTITY": 1,
    },
    "MDMA": {
        "BASE_PRICE": 30,
        "BASE_DANGER": 5,
        "BASE_QUANTITY": 5,
    },
    "Weed": {
        "BASE_PRICE": 10,
        "BASE_DANGER": 2,
        "BASE_QUANTITY": 10,
    }
}

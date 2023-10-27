from pydantic import BaseModel, Field

class DepositAccountsModels(BaseModel):
    id: str
    name: str
    accountHolderKey: str
    notes: str = ""
    accountHolderType: str = "CLIENT"
    accountState: str = "PENDING_APPROVAL"
    productTypeKey: str = "8ac981878a2b3c43018a2e72a5b3018d"
    accountType: str = "CURRENT_ACCOUNT"
    currencyCode: str = "MXN"
    assignedBranchKey: str = "8ac983b988fc977101890301c4060084"
    internalControls: dict = Field(
        {
            "recommendedDepositAmount": 2000000.0000000000,
            "maxWithdrawalAmount": 100000.0000000000
        }
    )
    overdraftSettings: dict = Field(
        {
            "allowOverdraft": False,
            "overdraftLimit": 0
        }
    )
    interestSettings: dict = Field(
        {
            "interestRateSettings": {
                "encodedKey": "8ac982208afedfb9018b0282eced0492",
                "interestChargeFrequency": "ANNUALIZED",
                "interestChargeFrequencyCount": 1,
                "interestRateTiers": [
                    {
                        "encodedKey": "8ac982208afedfb9018b0282eced0493",
                        "endingBalance": 0.9900000000,
                        "interestRate": 0
                    },
                    {
                        "encodedKey": "8ac982208afedfb9018b0282eced0494",
                        "endingBalance": 99999999.0000000000,
                        "interestRate": 9.00000000000000000000
                    }
                ],
                "interestRateTerms": "TIERED",
                "interestRateSource": "FIXED_INTEREST_RATE"
            },
            "interestPaymentSettings": {
                "interestPaymentPoint": "DAILY",
                "interestPaymentDates": []
            }
        }
    )
    overdraftInterestSettings: dict = {}
    balances: dict = Field(
        {
            "totalBalance": 0,
            "overdraftAmount": 0,
            "technicalOverdraftAmount": 0,
            "lockedBalance": 0,
            "availableBalance": 0,
            "holdBalance": 0,
            "overdraftInterestDue": 0,
            "technicalOverdraftInterestDue": 0,
            "feesDue": 0,
            "blockedBalance": 0,
            "forwardAvailableBalance": 0
        }
    )
    accruedAmounts: dict = Field(
        {
            "interestAccrued": 0,
            "overdraftInterestAccrued": 0,
            "technicalOverdraftInterestAccrued": 0,
            "negativeInterestAccrued": 0
        }
    )
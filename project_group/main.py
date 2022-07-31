import api, cash_on_hand, profit_loss, overheads

def main():
    '''
    combination of all functions
    '''
    # api functions
    api.apiwrite()
    # overheads functions
    overheads.high_heads()
    # cash on hand functions
    cash_on_hand.cash_def()
    cash_on_hand.cash_sur()
    # profit and loss functions
    profit_loss.net_def()
    profit_loss.net_sur()
print(main())

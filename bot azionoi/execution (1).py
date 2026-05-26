from config import TRANSACTION_COST
from risk_manager import calculate_position_size

def execute_buy(state, current_price, logger, current_date):
    '''
    esegue un acquisto simulato

    '''
    
    if state['position']==0:
        qty= calculate_position_size(state['capital'], current_price)
        
        if qty >0 :
            cost = qty * current_price
            fee= cost * TRANSACTION_COST
            total_cost = cost + fee
            
            if total_cost <= state['capital']:
                state['capital']-= total_cost
                state['position']=1
                state['shares']=qty 
                state["entry_price"]=current_price
                
                logger.info(f'BUY {qty} shares at {current_price:.2f} on {current_date}')
                print(f"[BUY]{qty} shares at {current_price:.2f}")
                
def execute_sell(state, current_price, logger, current_date):
    #vendita simulata 
    
    if state["position"] ==1:
        proceeds= state["shares"] * current_price
        fee= proceeds * TRANSACTION_COST
        net_proceeds = proceeds - fee
        state["capital"] += net_proceeds
        
        logger.info(f"SELL {state['shares']} shares at {current_price:.2f} on {current_date}")
        print(f"[SELL] {state['shares']} shares at {current_price: .2f}")
        
        state['position'] =0
        state['shares']=0
        state["entry_price"] =None
        
        
        
        
                
                
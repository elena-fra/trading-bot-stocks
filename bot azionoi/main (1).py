from config import INITIAL_CAPITAL, STOP_LOSS_PCT, TAKE_PROFIT_PCT
from logger_bot import setup_logger
from data_loader import load_data, create_features
from strategy import generate_signal
from execution import execute_buy, execute_sell


def check_stop_take(state, current_price, logger, current_date):
    '''
    controlla stop loss e take profit
    '''
    
    if state["position"]==1 and state["entry_price"] is not None:
        performance=(current_price - state["entry_price"]) / state["entry_price"]
        
        if performance <= -STOP_LOSS_PCT:
            logger.info(f"STOP LOSS triggered at {current_price:.2f} on {current_date}")
            execute_sell(state, current_price, logger, current_date)
            
        elif performance <= TAKE_PROFIT_PCT:
             logger.info(f"TAKE  PROFIT triggered at {current_price:2f} on {current_date}")
             execute_sell(state, current_price, logger, current_date)
             
             
def main():
    logger=setup_logger()
    
    state={
        "capital":INITIAL_CAPITAL,
        "position": 0,
        "shares":0,
        "entry_price":None
        }
    data= load_data()
    data=create_features(data)
    portfolio_values= []
    for idx, row in data.iterrows():
        current_price=row["Close"]
        current_date=idx.strftime("%Y-%m-%d")
        check_stop_take(state, current_price, logger,current_date)
        signal=generate_signal(row)
        
        if signal=="BUY":
            execute_buy(state, current_price, logger, current_date)
        elif signal =="SELL":
            execute_sell(state, current_price, logger, current_date)
            
            if state["position"]==1:
                portfolio_value=state["capital"]+state["shares"] * current_price
            else:
                portfolio_value=state["capital"]
                
            portfolio_values.append(portfolio_value)
                
        print("\n ===Risultati finali ====")
        print(f"Capitale finale :{state['capital']:.2f}")
        
        if len(portfolio_values)>0:
            print(f"Valore finale portafoglio: {portfolio_values[-1]:2f}")
            
            
main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
from config import ENTRY_THRESHOLD, EXIT_THRESHOLD

def generate_signal(row):
    '''
    genera un segnale operative 
    buy sell oppure hold
    '''
    
    if row['MA_FAST']> row["MA_SLOW"] and  row["Momentum_5"]> ENTRY_THRESHOLD: 
        return "BUY"
    elif row["MA_FAST"]< row["MA_SLOW"] or row["Momentum_5"]< EXIT_THRESHOLD:
        return "SELL"
    
    return "HOLD"
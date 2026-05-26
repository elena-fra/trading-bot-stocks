'''
class BrokerAPI:
    #classe base per collegamento a broker reali
    
    #symbol è l'assetto su chi vuoi operare, aapl, msft, btcusd
    #side indica il tipo di operazione  acquista = buy o vendi = sell 
    #quantity è la quantità di azione da comprare o da vendere
    #market = esegue subito al  miglior prezzo, limit esegue solo a un certo prezzo , stop esegue quando prezzo raggiunge una soglia
    
    def place_order(self,symbol, side, quantity, order_type="market"):
        print(f"Invio ordine {side} {quantity} {order_type}")
        
    def get_account_balance(self):
        return 0.0
    
    def get_open_positions(self):
        return[]
'''
from brokers.base_broker import baseBroker

class PaperBroker(baseBroker):
    '''
    broker simulato per paper trading
    tiene traccia di saldo , posizione e  ordini senza usare capitale reale 
    '''
    def __init__(self, initial_cash=10000.0, transaction_cost=0.001):
        self.cash= initial_cash
        self.transaction_cost= transaction_cost
        self.positions={}   #es {"AAPL": {"quantity":10, "entry_price":180.0}}
        self.order_history=[]
        
    def get_account_balance(self):
        #restituisce il saldo liquido disponibile
        return self.cash
    
    def get_open_positions(self):
        #restituisce la posizioni aperte
        return self.positions
    
    def place_order(self, symbol, side, quantity, price, order_type='market'):
        'simula un ordine buy o sell'
        
        if quantity <=0:
            return {"status": "rejected", "reason":"quantity must be > 0"}
        
        if side.upper()== "BUY":
            gross_cost=quantity * price
            fee = gross_cost * self.transaction_cost
            total_cost = gross_cost + fee
            
            if total_cost> self.cash:
                return {"status":"rejected", "resson":"insufficient cash"}
            
            self.cash-=total_cost
            
            if symbol in self.positions:
                old_qty = self.positions[symbol]["quantity"]
                old_entry= self.positions[symbol]["entry_price"]
                
                new_qty= old_qty + quantity
                new_entry=((old_qty * old_entry) + (quantity* price))/ new_qty
                
                self.positions[symbol]["quantity"] = new_qty
                self.positions[symbol]["entry_price"] = new_entry
            else:
                    self.positions[symbol]={
                        "quantity":quantity,
                        "entry_price":price}
                    
                    
                    order= {
                        "symbol" :symbol,
                        "side" : "BUY",
                        "quantity": quantity,
                        "price": price,
                        "fee":fee,
                        "status": "filled"}
                    
                    self.order_history.append(order)
                    return order 
        elif side.upper()=="SELL":
            if symbol not in self.positions:
                return {"status":"rejected", "reason": "not enough shares"}
            
            current_qty= self.positions[symbol]["quantity"]
            
            if quantity > current_qty:
                return {"status":"rejected", "reason":"not enough shares"}
            
            gross_proceeds=quantity * price 
            fee = gross_proceeds * self.transaction_cost
            net_proceeds= gross_proceeds -fee
            
            self.cash +=net_proceeds
            
            remaining_qty = current_qty - quantity
            
            
            if remaining_qty ==0:
                del self.positions[symbol]
            else:
                self.positions[symbol]["quantity"] = remaining_qty
                
            order = {
                "symbol":symbol,
                "side": "SELL",
                "quantity": quantity,
                "price" : price,
                "fee": fee,
                "status":"filled"
                }
            
            self.order_history.append(order)
            return order
        
        return {"status":"rejected", "reason":"invalid side"}
    
    def get_open_portfolio_value(self, market_price=None):
        ''' 
        restituisce il valore totale portafoglio
        se market_price è passato, valorizza anche la posizioe aperta
        '''
        total_value = self.cash
        
        if market_price is not None:
            for symbol, pos in self.position.items():
                total_value += pos["quantity"] * market_price
                
                
        return total_value
    
    def get_order_history(self):
        
        #restituisce la cronologia ordini
        
        return self.order_history
        
    
                

            
        
        
        
        
        
        













        
    
    
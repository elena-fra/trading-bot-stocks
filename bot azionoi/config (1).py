# configurazione generale

#asset da analizzare
TICKER="AAPL"

#periodo storico iniziale
START_DATE="2022-01-01"
END_DATE=None
#capitale iniziale simulato
INITIAL_CAPITAL= 10000.0

#gestione rischio
MAX_POSITION_SIZE=0.20
STOP_LOSS_PCT=0.03
TAKE_PROFIT_PCT=0.05

#costi di transazione
TRANSACTION_COST=0.001

#parametri strategia
ENTRY_THRESHOLD=0.002
EXIT_THRESHOLD=-0.001

#parametri medie mobili
FAST_MA=10
SLOW_MA=30

#cartella log
LOG_FOLDER="logs"
LOG_FILE="logs/trading.bot.log"













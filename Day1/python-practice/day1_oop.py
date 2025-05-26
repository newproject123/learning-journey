```python

Objects/Classes
class Trade:
  def __init__(self, price, quantity):
    self.price = price
    self.quantity = quantity
  def value(self):
    return self.price * self.quantity

t1 = Trade("AAPL", 100, 187.25)
print(f"Trade value: ${t1.value():,.2f}")


Encapsulation
class Portfolio:
    def __init__(self):
        self._trades = []  # private list of trades

    def add_trade(self, trade):
        if isinstance(trade, Trade):
            self._trades.append(trade)
        else:
            raise TypeError("Must add a Trade object")

    def total_value(self):
        return sum(t.value() for t in self._trades)

    def list_symbols(self):
        return [t.symbol for t in self._trades]

p = Portfolio()
p.add_trade(Trade("AAPL", 100, 187.25))
p.add_trade(Trade("TSLA", 50, 200))

print(f"Total portfolio value: ${p.total_value():,.2f}")
print("Symbols:", p.list_symbols())

Polymorphism/Inheritance
class Trade:
    def __init__(self, symbol, qty, price):
        self.symbol = symbol
        self.qty = qty
        self.price = price

    def value(self):
        return self.qty * self.price

class OptionTrade(Trade):
    def __init__(self, symbol, qty, price, strike, expiry):
        super().__init__(symbol, qty, price)
        self.strike = strike
        self.expiry = expiry

    def is_expired(self, current_date):
        return current_date > self.expiry
      
    def value(self):
        return self.qty * max(0, self.price - self.strike)

Dunder methods

class Trade:
    def __init__(self, symbol, qty, price):
        self.symbol = symbol
        self.qty = qty
        self.price = price

    def value(self):
        return self.qty * self.price

    def __str__(self):
        return f"Trade({self.symbol}, qty={self.qty}, price={self.price})"

    def __add__(self, other):
        if isinstance(other, Trade) and self.symbol == other.symbol:
            return Trade(self.symbol, self.qty + other.qty, self.price)
        else:
            raise ValueError("Can only add Trade objects with the same symbol")

```

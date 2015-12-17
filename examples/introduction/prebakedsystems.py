from systems.provided.example.simplesystem import simplesystem

my_system = simplesystem()
print(my_system)
print(my_system.portfolio.get_notional_position("EDOLLAR").tail(5))

from sysdata.csvdata import csvFuturesData
from sysdata.configdata import Config

"""
Now loading config and data
"""

my_config = Config("systems.provided.example.simplesystemconfig.yaml")
my_data = csvFuturesData()
my_system = simplesystem(config=my_config, data=my_data)
print(my_system.portfolio.get_notional_position("EDOLLAR").tail(5))


"""
Let's get the chapter 15 system
"""

from systems.provided.futures_chapter15.basesystem import futures_system

system = futures_system()

print(system.portfolio.get_notional_position("EUROSTX").tail(5))

system.accounts.portfolio().stats()
system.accounts.pandl_for_instrument("US10").curve().plot()
from matplotlib.pyplot import show
show()
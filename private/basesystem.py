'''
This is a futures system

A system consists of a system, plus a config

'''
from sysdata.csvdata import csvFuturesData
from sysdata.configdata import Config

from systems.forecasting import Rules
from systems.basesystem import System
from systems.forecast_combine import ForecastCombineFixed
from systems.forecast_scale_cap import ForecastScaleCapFixed
from systems.futures.rawdata import FuturesRawData
from systems.positionsizing import PositionSizing
from systems.portfolio import PortfoliosFixed
from systems.account import Account


def futures_system(data=None, config=None, trading_rules=None, log_level="on"):
    if data is None:
        data = csvFuturesData()

    if config is None:
        config = Config(
            "private.futuresconfig.yaml")

    rules = Rules(trading_rules)

    components = [Account(),
                  PortfoliosFixed(),
                  PositionSizing(),
                  FuturesRawData(),
                  ForecastCombineFixed(),
                  ForecastScaleCapFixed(),
                  rules]

    system = System(components, data, config)
    system.set_logging_level(log_level)
    return system


if __name__ == '__main__':
    import doctest
    doctest.testmod()

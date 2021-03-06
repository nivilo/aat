
class StrategyManagerPortfolioMixin(object):
    # *********************
    # Risk Methods        *
    # *********************
    def portfolio(self):
        return self._portfolio_mgr.portfolio()

    def positions(self, instrument=None, exchange=None):
        return self._portfolio_mgr.positions(instrument=instrument, exchange=exchange)

    def priceHistory(self, instrument=None):
        return self._portfolio_mgr.priceHistory(instrument=instrument)

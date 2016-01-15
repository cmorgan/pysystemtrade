
def compare(systems, metric='curve'):
    ax = None
    for sys in systems:
        portfolio = sys.accounts.portfolio()
        metric_obj = getattr(portfolio, metric)

        if ax is None:
            ax = metric_obj().plot(title=metric)
        else:
            metric_obj().plot(ax=ax)
    return ax

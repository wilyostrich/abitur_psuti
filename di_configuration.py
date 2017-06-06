import dependency_injector as di

class DIConfige(di.AbstractCatalog):
    config_ini = di.Provider()

class DIBot(di.AbstractCatalog):
    di_bot = di.Provider()
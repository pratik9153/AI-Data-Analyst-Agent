class DataAnalystError(Exception):
    pass


class InvalidDataError(DataAnalystError):
    pass


class EmptyDataError(DataAnalystError):
    pass


class AnalysisError(DataAnalystError):
    pass
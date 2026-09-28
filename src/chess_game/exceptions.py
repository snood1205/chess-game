class InvalidMoveError(Exception):
    """Not to be directly raised/instantiated, only for catching"""

    pass


class PromotionError(InvalidMoveError):
    pass

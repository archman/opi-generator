

class Rule(object):

    def __init__(self, prop_id):
        self._prop_id = prop_id


class BetweenRule(Rule):

    def __init__(self, prop_id, pv, min, max):
        super(BetweenRule, self).__init__(prop_id)
        self._pv = pv
        self._min = min
        self._max = max


class GreaterThanRule(Rule):

    def __init__(self, prop_id, pv, threshold):
        super(GreaterThanRule, self).__init__(prop_id)
        self._pv = pv
        self._threshold = threshold

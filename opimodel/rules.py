

class Rule(object):

    def __init__(self, prop_id):
        self._prop_id = prop_id


class BetweenRule(Rule):

    def __init__(self, prop_id, pv, min_val, max_val,
             gt_equals=False, lt_equals=False):

        super(BetweenRule, self).__init__(prop_id)
        self._pv = pv
        self._min = min_val
        self._max = max_val
        self._lt_equals = lt_equals
        self._gt_equals = gt_equals


class GreaterThanRule(Rule):

    def __init__(self, prop_id, pv, threshold):
        super(GreaterThanRule, self).__init__(prop_id)
        self._pv = pv
        self._threshold = threshold

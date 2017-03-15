

class RuleModel(object):

    def __init__(self, prop_id):
        self._prop_id = prop_id


class BetweenRuleModel(RuleModel):

    def __init__(self, prop_id, pv, min, max):
        super(BetweenRuleModel, self).__init__(prop_id)
        self._pv = pv
        self._min = min
        self._max = max


class GreaterThanRuleModel(RuleModel):

    def __init__(self, prop_id, pv, threshold):
        super(GreaterThanRuleModel, self).__init__(prop_id)
        self._pv = pv
        self._threshold = threshold

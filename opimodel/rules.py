

class Rule(object):

    def __init__(self, prop_id, name=None):
        self._prop_id = prop_id
        if name is not None:
            self._name = name


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


class SelectionRule(Rule):

    def __init__(self, prop_id, pv, options, var="pv0"):
        """

        :param prop_id: Widget property to set
        :param pv: Controlling PV
        :param options: List of tuples (value, widget value)
        :param var: Variable to use (pv0 for value, pvSevr0 for alarm severity)
        """
        super(SelectionRule, self).__init__(prop_id)
        self._pv = pv
        self._options = options
        self._var = var
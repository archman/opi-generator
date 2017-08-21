
PV_VAL = "pv0"
PV_SEVR = "pvSev0"


class Rule(object):

    def __init__(self, prop_id, name=None):
        """

        Args:
            prop_id: Widget property to set
            pv: Controlling PV
            name (optional): Rule Name as displayed in CSS OPIEditor
        """
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

    def __init__(self, prop_id, pv, options, var=PV_VAL):
        """ Simple selection rule, e.g.:

            widget.rules = []
            options = [(-1, colors.INVALID), (1, colors.MAJOR), (2, colors.MINOR)]
            widget.rules.append(
                rules.SelectionRule('on_color', pv_name, options, var=PV_SEVR))

        Args:
            prop_id: Widget property to set
            pv: Controlling PV
            options: List of tuples (value, widget value)
            var: Variable to use (pv0 for value, pvSev0 for alarm severity)
        """
        super(SelectionRule, self).__init__(prop_id)
        self._pv = pv
        self._options = options
        self._var = var
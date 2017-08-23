
PV_VAL = "pv0"
PV_SEVR = "pvSev0"


class Rule(object):

    def __init__(self, prop_id, name=None):
        """ Base class for rules.

            If no `name` is provided the Rule class name is used.
        Args:
            prop_id: Widget property to set
            pv: Controlling PV
            name (optional): Rule Name as displayed in CSS OPIEditor
        """
        self._prop_id = prop_id
        self._name = type(self).__name__ if name is None else name


class BetweenRule(Rule):

    def __init__(self, prop_id, pv, min_val, max_val,
             min_equals=True, max_equals=True, name=None):
        """ Construct an rule setting the specified boolean property
                - True if min_val <= pv <= max_val
                - False otherwise

            If min_equals is false the lower limit is replaced by '<'
            If max_equals is false the upper limit is replaced by '<'

        Args:
            prop_id: Widget property to set
            pv: Controlling PV
            min_val: Lower bound
            max_val: Upper bound
            min_equals: True if range is inclusive at lower end
            max_equals: True if range is inclusive at upper end
            name (optional): Rule Name as displayed in CSS OPIEditor
        """
        super(BetweenRule, self).__init__(prop_id, name)
        self._pv = pv
        self._min = min_val
        self._max = max_val
        self._min_equals = min_equals
        self._max_equals = max_equals


class GreaterThanRule(Rule):

    def __init__(self, prop_id, pv, threshold, name=None):
        """ Construct an rule setting the specified boolean property
                - True if pv > threshold
                - False otherwise

        Args:
            prop_id: Widget property to set
            pv: Controlling PV
            threshold: Threshold value
            name (optional): Rule Name as displayed in CSS OPIEditor
        """
        super(GreaterThanRule, self).__init__(prop_id, name)
        self._pv = pv
        self._threshold = threshold


class SelectionRule(Rule):

    def __init__(self, prop_id, pv, options, var=PV_VAL, name=None):
        """ Simple selection rule setting specified property to one of a
            number of possible values based on the pv value, e.g.:

            widget.rules = []
            options = [(-1, colors.INVALID), (1, colors.MAJOR), (2, colors.MINOR)]
            widget.rules.append(
                rules.SelectionRule('on_color', pv_name, options, var=PV_SEVR))

        Args:
            prop_id: Widget property to set
            pv: Controlling PV
            options: List of tuples (value, widget value)
            var: Variable to use (pv0 for value, pvSev0 for alarm severity)
            name (optional): Rule Name as displayed in CSS OPIEditor
        """
        super(SelectionRule, self).__init__(prop_id, name)
        self._pv = pv
        self._options = options
        self._var = var

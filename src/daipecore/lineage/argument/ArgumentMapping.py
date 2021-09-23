from daipecore.lineage.argument.ArgumentMappingInterface import ArgumentMappingInterface
from daipecore.lineage.argument.GetWidgetValue import GetWidgetValue


class ArgumentMapping(ArgumentMappingInterface):
    def get_mapping(self):
        return {
            "get_widget_value": GetWidgetValue,
        }

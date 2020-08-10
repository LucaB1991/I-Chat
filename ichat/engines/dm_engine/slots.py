from typing import Any, Dict, Text, Type, NoReturn
from ichat.utils.exceptions import IChatError


class Slot:
    """Base class for info storage throughout the conversation. It works side by side the entity concept"""
    category = "root"

    @staticmethod
    def search_by_category(slot_category: Text) -> Type["Slot"]:
        """Returns a slot instance given its category"""
        for sub_cls in extract_all_subclasses(Slot):  # 1° attempt
            if sub_cls.category == slot_category:
                return sub_cls
        try:  # 2° attempt
            return extract_class_from_module_path(slot_category)
        except (ImportError, AttributeError):
            raise IChatError("Failed to find slot category, '{}'".format(slot_category))

    def __init__(self,
                 name: Text,
                 initial_value: Any = None,
                 enable_auto_filling: bool = True
                 ) -> None:
        """Constructor"""
        self._name = name
        self._initial_value = initial_value
        self._current_value = initial_value
        self._enable_auto_filling = enable_auto_filling
        self._features_dimensionality = 0  # -> no features...

    @property
    def name(self) -> Text:
        return self._name

    @property
    def current_value(self) -> Any:
        return self._current_value

    @current_value.setter
    def current_value(self, value: Any) -> None:
        self._current_value = value

    def reset_value(self) -> None:
        self._current_value = self._initial_value

    def get_features_dimensions(self) -> int:
        """self explanatory"""
        return self._features_dimensionality

    def has_features(self) -> bool:
        return self.get_features_dimensions() != 0

    def as_feature(self) -> NoReturn:
        raise NotImplementedError("Every slot must implement this method")

    def info(self) -> Dict[Text, Any]:
        return {
            'category': None,
            'initial_value': self._initial_value,
            'enable_auto_filling': self._enable_auto_filling
        }

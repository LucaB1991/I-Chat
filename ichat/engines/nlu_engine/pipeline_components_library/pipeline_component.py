from typing import Any, Dict, Text, List, Type, Optional


class PipelineComponent:
    """Base class for custom natural language understanding pipeline component"""

    @classmethod
    def dependencies(cls) -> Dict[Text, Any]:
        return {
            'packages': cls.get_required_packages(),
            'components': cls.get_required_components()
        }

    def __init__(self, component_configuration: Optional[Dict[Text, Any]] = None) -> None:
        pass

    def train(self) -> None:
        """Trains the component"""
        pass

    def process(self) -> None:
        """Process incoming unknown data"""
        pass

    def store(self) -> None:
        """Stores component data for future reload"""
        pass


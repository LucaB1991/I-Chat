from typing import Any, Dict, Text


class Domain:
    """It describes the system universe. All actions, intents and entities must be defined within the domain"""

    @classmethod
    def create_empty(cls) -> "Domain":
        """Custom constructor. It creates an empty domain."""
        return cls()

    def __init__(self,
                 user_intents,
                 entities,
                 slots,
                 responses_templates,
                 actions,
                 forms,
                 store_entities_as_slots: bool = True
                 ) -> None:
        self.entities = entities
        self.slots = slots
        self.response_templates = responses_templates
        self.store_entities_as_slots = store_entities_as_slots

    def combine_with(self, other_domain: "Domain") -> "Domain":
        pass

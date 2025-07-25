from abc import ABC, abstractmethod

class KnowledgeService(ABC):
    
    @abstractmethod
    async def initialize(self) -> None:
        """Initialize the knowledge service."""
        pass

    @abstractmethod
    async def _load_data(self) -> None:
        """Load data from the source."""
        pass
    
    @abstractmethod
    async def _process_data(self) -> None:
        """Process the loaded documents."""
        pass
    
    @abstractmethod
    async def reload_data(self) -> None:
        """Reload the data from the source."""
        pass
    
    @abstractmethod
    async def close(self) -> None:
        """Close the knowledge service."""
        pass
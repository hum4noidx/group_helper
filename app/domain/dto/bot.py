from domain.dto.base import DTO


class BotDTO(DTO):
    """ DTO for class BotSettings model """
    id: int = 1
    status: str = 'normal'

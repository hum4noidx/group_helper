from domain.dto.base import DTO


class BadWordDTO(DTO):
    id: int
    word: str
    used_count: int

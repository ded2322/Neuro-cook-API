from pydantic import BaseModel


class SComment(BaseModel):
    text_comment: str
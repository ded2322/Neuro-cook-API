from pydantic import BaseModel


class SPost(BaseModel):
    name_recipe: str
    text_post: str
    text_preview: str

    class Config:
        from_attributes = True



from pydantic import BaseModel


class BackTaskItem(BaseModel):
    lw_type: int
    file_name: str
    file_content: bytes
    tenant_id: str
    biz_id: str
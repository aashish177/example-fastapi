"""empty message

Revision ID: 0492fb3116be
Revises: e7cf3be8e3e5
Create Date: 2024-12-25 14:55:32.330164

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0492fb3116be'
down_revision: Union[str, None] = 'e7cf3be8e3e5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

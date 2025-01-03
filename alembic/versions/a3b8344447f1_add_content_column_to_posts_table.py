"""Add content column to posts table

Revision ID: a3b8344447f1
Revises: 963f541e727d
Create Date: 2024-12-25 14:23:41.200479

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a3b8344447f1'
down_revision: Union[str, None] = '963f541e727d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass

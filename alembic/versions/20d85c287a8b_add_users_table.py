"""Add users table

Revision ID: 20d85c287a8b
Revises: a3b8344447f1
Create Date: 2024-12-25 14:28:01.601026

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20d85c287a8b'
down_revision: Union[str, None] = 'a3b8344447f1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.Integer(), nullable=False),
                    sa.Column('password', sa.Integer(), nullable=False),
                    sa.Column('create_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass

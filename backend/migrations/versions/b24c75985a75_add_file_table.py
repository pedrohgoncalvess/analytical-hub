"""add: file table

Revision ID: b24c75985a75
Revises: 
Create Date: 2024-03-01 00:06:25.047312

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'b24c75985a75'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("create schema if not exists file")
    op.create_table('file',
    sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
    sa.Column('name', sa.String(length=150), nullable=False, unique=True),
    sa.Column('type', sa.String(length=10), nullable=False),
    sa.Column('size', sa.Numeric(), nullable=False),
    sa.Column('nb_columns', sa.Integer(), nullable=False),
    sa.Column('nb_rows', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.text("now()")),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=False, server_default=sa.text("true")),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    schema='file'
    )


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('drop table file.file')
    op.execute("drop schema if not exists file cascade")
    # ### end Alembic commands ###

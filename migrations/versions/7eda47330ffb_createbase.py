"""CreateBase

Revision ID: 7eda47330ffb
Revises: 
Create Date: 2023-11-24 17:02:21.263266

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '7eda47330ffb'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('category',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('category', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('comics',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('autor', sa.String(), nullable=True),
                    sa.Column('year', sa.String(), nullable=True),
                    sa.Column('comics_id', sa.Integer(), nullable=True),
                    )
    op.create_table('publishings',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('publishings_id', sa.Integer(), nullable=True),
                    )
    op.create_table('genres',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('genres_id', sa.Integer(), nullable=True),
                    )
    op.create_table('series',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('series_id', sa.Integer(), nullable=True),
                    )
    op.create_table('personajs',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('personajs_id', sa.Integer(), nullable=True),
                    )


def downgrade() -> None:
    op.drop_table('comics_publishings')
    op.drop_table('comics')
    op.drop_table('publishings')
    op.drop_table('genres')
    op.drop_table('series')
    op.drop_table('personajs')

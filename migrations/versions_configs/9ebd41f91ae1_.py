"""empty message

Revision ID: 9ebd41f91ae1
Revises: 
Create Date: 2024-04-25 04:48:47.311702

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9ebd41f91ae1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Guild',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Race',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Spec',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('User',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('RaceSpec',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('race_id', sa.Integer(), nullable=False),
    sa.Column('spec_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['race_id'], ['Race.id'], ),
    sa.ForeignKeyConstraint(['spec_id'], ['Spec.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Character',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nickname', sa.String(length=100), nullable=False),
    sa.Column('level', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('id_racespec', sa.Integer(), nullable=False),
    sa.Column('id_guild', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_guild'], ['Guild.id'], ),
    sa.ForeignKeyConstraint(['id_racespec'], ['RaceSpec.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Character')
    op.drop_table('RaceSpec')
    op.drop_table('User')
    op.drop_table('Spec')
    op.drop_table('Race')
    op.drop_table('Guild')
    # ### end Alembic commands ###

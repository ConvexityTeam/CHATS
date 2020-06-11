"""empty message

Revision ID: e39034267077
Revises: a34d3669ecff
Create Date: 2020-06-11 12:11:40.676108

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e39034267077'
down_revision = 'a34d3669ecff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('synchronization_filter',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.Column('contract_address', sa.String(), nullable=True),
    sa.Column('contract_type', sa.String(), nullable=True),
    sa.Column('last_block_synchronized', sa.Integer(), nullable=True),
    sa.Column('filter_parameters', sa.String(), nullable=True),
    sa.Column('filter_type', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('synchronization_filter')
    # ### end Alembic commands ###

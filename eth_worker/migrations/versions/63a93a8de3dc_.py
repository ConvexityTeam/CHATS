"""empty message

Revision ID: 63a93a8de3dc
Revises: c13b0a18676d
Create Date: 2019-10-26 15:23:24.415903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63a93a8de3dc'
down_revision = 'c13b0a18676d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blockchain_transaction', sa.Column('contract_address', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blockchain_transaction', 'contract_address')
    # ### end Alembic commands ###

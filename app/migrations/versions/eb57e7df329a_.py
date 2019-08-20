"""empty message

Revision ID: eb57e7df329a
Revises: 4527fe5c9b99
Create Date: 2018-10-10 18:00:43.422863

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb57e7df329a'
down_revision = '4527fe5c9b99'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('terms_accepted', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'terms_accepted')
    # ### end Alembic commands ###

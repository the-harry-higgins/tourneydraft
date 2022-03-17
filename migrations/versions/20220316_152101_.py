"""empty message

Revision ID: a83e91e68541
Revises: 5072546c208c
Create Date: 2022-03-16 15:21:01.391901

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a83e91e68541'
down_revision = '5072546c208c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'tournaments', ['year'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tournaments', type_='unique')
    # ### end Alembic commands ###

"""empty message

Revision ID: aa65f8a4ddaa
Revises: c2e36a325896
Create Date: 2021-02-19 21:22:07.029556

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa65f8a4ddaa'
down_revision = 'c2e36a325896'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'Shows', ['start_time'])
    op.create_unique_constraint(None, 'Shows', ['venue_id'])
    op.create_unique_constraint(None, 'Shows', ['artist_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Shows', type_='unique')
    op.drop_constraint(None, 'Shows', type_='unique')
    op.drop_constraint(None, 'Shows', type_='unique')
    # ### end Alembic commands ###

"""empty message

Revision ID: 1acfc8df1013
Revises: 1aac1ae7d26b
Create Date: 2021-02-07 09:25:34.904676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1acfc8df1013'
down_revision = '1aac1ae7d26b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'completed',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'completed',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###

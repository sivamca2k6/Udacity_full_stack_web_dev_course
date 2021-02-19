"""empty message

Revision ID: 0770988a21ac
Revises: c0b083df8105
Create Date: 2021-02-19 22:11:16.834778

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0770988a21ac'
down_revision = 'c0b083df8105'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Shows',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['Venue.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('venue_id', 'artist_id', 'start_time', name='unique_constraint_11')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Shows')
    # ### end Alembic commands ###

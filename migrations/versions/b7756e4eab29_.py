"""empty message

Revision ID: b7756e4eab29
Revises: 441975213ebc
Create Date: 2021-03-12 15:54:29.041921

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7756e4eab29'
down_revision = '441975213ebc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('booking_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('address', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=80), nullable=True),
    sa.Column('imagePath', sa.String(length=500), nullable=True),
    sa.Column('price', sa.String(length=100), nullable=True),
    sa.Column('isAvailable', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('booking')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('booking',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='booking_pkey')
    )
    op.drop_table('booking_info')
    # ### end Alembic commands ###

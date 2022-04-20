"""Users can be admins

Revision ID: 72ddb1e97dfd
Revises: 
Create Date: 2020-03-24 16:22:28.296990

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72ddb1e97dfd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_admin', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_admin')
    # ### end Alembic commands ###

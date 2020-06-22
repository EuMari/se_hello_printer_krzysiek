"""aboutme

Revision ID: 19da28aa4fc5
Revises: f5166568f563
Create Date: 2020-06-06 15:32:51.437887

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19da28aa4fc5'
down_revision = 'f5166568f563'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('aboutme', sa.String(length=140), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'aboutme')
    # ### end Alembic commands ###
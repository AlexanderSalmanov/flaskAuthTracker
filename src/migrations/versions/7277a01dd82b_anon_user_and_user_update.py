"""anon_user_and_user_update

Revision ID: 7277a01dd82b
Revises: 6cc4a4ff9209
Create Date: 2023-12-03 12:15:49.048701

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7277a01dd82b'
down_revision = '6cc4a4ff9209'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('anonymous_user',
    sa.Column('ip_address', sa.String(length=50), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('interactions_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ip_address')
    )
    op.add_column('user', sa.Column('interactions_count', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'interactions_count')
    op.drop_table('anonymous_user')
    # ### end Alembic commands ###

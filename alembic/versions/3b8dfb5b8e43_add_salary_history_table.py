"""add salary history table

Revision ID: 3b8dfb5b8e43
Revises: 8b3930abe62b
Create Date: 2020-09-26 14:36:52.654708

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b8dfb5b8e43'
down_revision = '8b3930abe62b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'salary_history',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('eid', sa.Integer, nullable=False, index=True),
        sa.Column('salary', sa.Integer, nullable=False),
        sa.Column('date', sa.Date, nullable=False),
    )

def downgrade():
    op.drop_table('salary_history')

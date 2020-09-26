"""create employee_directory table

Revision ID: 8b3930abe62b
Revises: 
Create Date: 2020-09-26 12:49:56.767027

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b3930abe62b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'employee_directory',
        sa.Column('eid', sa.Integer, primary_key=True),
        sa.Column('name', sa.Unicode(255), nullable=False),
        sa.Column('gender', sa.String(1), nullable=False),
        sa.Column('hire_date', sa.Date, nullable=False),
        sa.Column('department', sa.Unicode(255), nullable=False),
        sa.Column('division', sa.Unicode(255), nullable=False),
        sa.Column('jobcode', sa.Unicode(255), nullable=False),
        sa.Column('manager', sa.Unicode(255), nullable=False),
        sa.Column('performance', sa.Unicode(255), nullable=False),
        sa.Column('annual_benefits_value', sa.Unicode(255), nullable=False),
    )

def downgrade():
    op.drop_table('employee_directory')
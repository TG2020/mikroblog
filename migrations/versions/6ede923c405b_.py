"""empty message

Revision ID: 6ede923c405b
Revises: 9b0db1fdc0e3
Create Date: 2024-06-25 18:11:27.079117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ede923c405b'
down_revision = '9b0db1fdc0e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('birth_date', sa.String(length=10), nullable=True),
    sa.Column('nationality', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('author', sa.String(length=64), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('genre', sa.String(length=64), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('loan',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('borrower_name', sa.String(length=64), nullable=True),
    sa.Column('loan_date', sa.Date(), nullable=True),
    sa.Column('due_date', sa.Date(), nullable=True),
    sa.Column('returned', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('return',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('loan_id', sa.Integer(), nullable=True),
    sa.Column('return_date', sa.Date(), nullable=True),
    sa.Column('fine', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['loan_id'], ['loan.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('return')
    op.drop_table('loan')
    op.drop_table('book')
    op.drop_table('author')
    # ### end Alembic commands ###
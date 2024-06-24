from alembic import op
import sqlalchemy as sa



revision = '9b0db1fdc0e3'
down_revision = '3aa7d09e0977'
branch_labels = None
depends_on = None


def upgrade():

    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_created'), 'post', ['created'], unique=False)



def downgrade():

    op.drop_index(op.f('ix_post_created'), table_name='post')
    op.drop_table('post')

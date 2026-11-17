"""webhooklar: Discord sunucu davet bağlantısı

Revision ID: 0007_webhook_davet
Revises: 0006_webhook_discord_bilgisi
"""
from alembic import op
import sqlalchemy as sa


revision = '0007_webhook_davet'
down_revision = '0006_webhook_discord_bilgisi'
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table('webhooklar') as batch_op:
        batch_op.add_column(sa.Column('davet', sa.String(length=100), nullable=True))


def downgrade() -> None:
    with op.batch_alter_table('webhooklar') as batch_op:
        batch_op.drop_column('davet')

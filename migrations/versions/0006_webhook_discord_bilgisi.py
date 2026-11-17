"""webhooklar: Discord webhook'larının sunucu/kanal bilgisi

Revision ID: 0006_webhook_discord_bilgisi
Revises: 0005_webhooklar
"""
from alembic import op
import sqlalchemy as sa


revision = '0006_webhook_discord_bilgisi'
down_revision = '0005_webhooklar'
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table('webhooklar') as batch_op:
        batch_op.add_column(sa.Column('discord_bilgisi', sa.JSON(), nullable=True))
        batch_op.add_column(sa.Column('discord_bilgisi_zamani', sa.DateTime(timezone=True), nullable=True))


def downgrade() -> None:
    with op.batch_alter_table('webhooklar') as batch_op:
        batch_op.drop_column('discord_bilgisi_zamani')
        batch_op.drop_column('discord_bilgisi')

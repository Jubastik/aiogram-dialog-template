from aiogram.types import Message
from aiogram_dialog import DialogProtocol, DialogManager

from app.db.db_user.user_func import User


async def handle_name(message: Message, dialog: DialogProtocol, manager: DialogManager):
    manager.dialog_data["name"] = message.text
    await User.register(message.from_user.id, message.text)
    await manager.done()

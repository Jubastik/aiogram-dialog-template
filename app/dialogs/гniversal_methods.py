from aiogram_dialog import DialogManager


def get_tg_id_from_manager(dialog_manager: DialogManager):
    return dialog_manager.event.from_user.id

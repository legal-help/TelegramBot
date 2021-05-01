from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import go_callback


# Направления обучения
choice = InlineKeyboardMarkup(row_width=1)

go_bakalavr = InlineKeyboardButton(text='Бакалавриат/специалитет', callback_data='go:bakalavr')
choice.insert(go_bakalavr)

go_magistr = InlineKeyboardButton(text='Магистратура', callback_data='go:magistr')
choice.insert(go_magistr)

go_contact = InlineKeyboardButton(text='Контакты', callback_data='go:contact')
choice.insert(go_contact)

# TODO: Подумать нужна ли отмена в основном меню
# cancel_button = InlineKeyboardButton(text='Отмена', callback_data='cancel')
# choice.insert(cancel_button)


# Очная форма обучения
b_ochnaya_keyboard = InlineKeyboardMarkup(row_width=1)

go_b_budget = InlineKeyboardButton(text='Бюджет', callback_data='go:b_budget')
b_ochnaya_keyboard.insert(go_b_budget)

go_b_pay = InlineKeyboardButton(text='Платное', callback_data='go:b_pay')
b_ochnaya_keyboard.insert(go_b_pay)

b_cancel_button = InlineKeyboardButton(text='Отмена', callback_data='go:b_cancel')
b_ochnaya_keyboard.insert(b_cancel_button)

# Магистратура
magistratura_keyboard = InlineKeyboardMarkup(row_width=1)

go_m_budget = InlineKeyboardButton(text='Бюджет', callback_data='go:m_budget')
magistratura_keyboard.insert(go_m_budget)

go_m_pay = InlineKeyboardButton(text='Платное', callback_data='go:m_pay')
magistratura_keyboard.insert(go_m_pay)

m_cancel_button = InlineKeyboardButton(text='Отмена', callback_data='go:m_cancel')
magistratura_keyboard.insert(m_cancel_button)

# Бюджетная магистратура (m_budget - mb)
m_budget_keyboard = InlineKeyboardMarkup(row_width=1)

go_mb_directions = InlineKeyboardButton(text='Направления', callback_data='go:mb_directions')
m_budget_keyboard.insert(go_mb_directions)

go_mb_documents = InlineKeyboardButton(text='Документы', callback_data='go:mb_documents')
m_budget_keyboard.insert(go_mb_documents)

go_mb_stages = InlineKeyboardButton(text='Этапы зачисления (сроки)', callback_data='go:mb_stages')
m_budget_keyboard.insert(go_mb_stages)

# Направления бюджетной магистратуры (mb_directions - mbd)
mb_directions_keyboard = InlineKeyboardMarkup(row_width=1)

go_mbd_tpp = InlineKeyboardButton(text='Теория и практика конституционного правопользования', callback_data='go:mbd_tpp')
mb_directions_keyboard.insert(go_mbd_tpp)

go_mbd_apppd = InlineKeyboardButton(text='Актуальные проблемы правозащитной и правоохранительной деятельности', callback_data='go:mbd_apppd')
mb_directions_keyboard.insert(go_mbd_apppd)

# Документы бюджетной магистратуры (mb_documents - mbs)

mb_documents_keyboard = InlineKeyboardMarkup(row_width=1)

go_mbdoc_subjects = InlineKeyboardButton(text='Предметы', callback_data='go:mbdoc_subjects')
mb_documents_keyboard.insert(go_mbdoc_subjects)

go_mbdoc_programm = InlineKeyboardButton(text='Программа вступительных испытаний', callback_data='go:mbdoc_programm')
mb_documents_keyboard.insert(go_mbdoc_programm)

go_mbdoc_documents = InlineKeyboardButton(text='Перечень документов для поступления', callback_data='go:mbdoc_documents')
mb_documents_keyboard.insert(go_mbdoc_documents)

go_mbdoc_terms = InlineKeyboardButton(text='Сроки подачи документов', callback_data='go:mbdoc_terms')
mb_documents_keyboard.insert(go_mbdoc_terms)

go_bmdoc_points = InlineKeyboardButton(text='Премиальные баллы по индивидуальным достижениям', callback_data='go:bmdoc_points')
mb_documents_keyboard.insert(go_bmdoc_points)

# Этапы зачисления бюджетной магистратуры (mb_stages - mbs)

mb_stages_keyboard = InlineKeyboardMarkup(row_width=1)

go_mbs_enrollment = InlineKeyboardButton(text='Зачисление', callback_data='go:mbs_enrollment')
mb_stages_keyboard.insert(go_mbs_enrollment)

go_mbs_original = InlineKeyboardButton(text='Прием оригиналов документов', callback_data='go:mbs_original')
mb_stages_keyboard.insert(go_mbs_original)

go_mbs_publication = InlineKeyboardButton(text='Публикация конкурсных списков', callback_data='go:mbs_publication')
mb_stages_keyboard.insert(go_mbs_publication)

go_mbs_order = InlineKeyboardButton(text='Издание приказа о зачислении', callback_data='go:mbs_order')
mb_stages_keyboard.insert(go_mbs_order)


# Зачисление (mbs_enrollmen - mbse)
mbs_enrollment_keyboard = InlineKeyboardMarkup(row_width=1)

go_mbse_priority = InlineKeyboardButton(text='Этап приоритетного зачисления', callback_data='go:mbse_priority')
mbs_enrollment_keyboard.insert(go_mbse_priority)

go_mbse_base = InlineKeyboardButton(text='Основной этап зачисления', callback_data='go:mbse_base')
mbs_enrollment_keyboard.insert(go_mbse_base)

# Платная магистратура (mp)
m_pay_keyboard = InlineKeyboardMarkup(row_width=1)

go_mp_directions = InlineKeyboardButton(text='Направления', callback_data='go:mp_directions')
m_pay_keyboard.insert(go_mp_directions)

go_mp_documents = InlineKeyboardButton(text='Документы', callback_data='go:mp_documents')
m_pay_keyboard.insert(go_mp_documents)

go_mp_stages = InlineKeyboardButton(text='Этапы зачисления (сроки)', callback_data='go:mp_stages')
m_pay_keyboard.insert(go_mp_stages)

# Направления платной магистратуры (mp_directions - mpd)
mp_directions_keyboard = InlineKeyboardMarkup(row_width=1)

go_mpd_tpp = InlineKeyboardButton(text='Теория и практика конституционного правопользования', callback_data='go:mpd_tpp')
mp_directions_keyboard.insert(go_mpd_tpp)

go_mpd_apppd = InlineKeyboardButton(text='Актуальные проблемы правозащитной и правоохранительной деятельности', callback_data='go:mpd_apppd')
mp_directions_keyboard.insert(go_mpd_apppd)

# Документы платной магистратуры (повторяются колбэки бюджетной магистратуры)

mp_documents_keyboard = InlineKeyboardMarkup(row_width=1)

go_mpdoc_subjects = InlineKeyboardButton(text='Предметы', callback_data='go:mpdoc_subjects')
mp_documents_keyboard.insert(go_mpdoc_subjects)

go_mpdoc_programm = InlineKeyboardButton(text='Программа вступительных испытаний', callback_data='go:mpdoc_programm')
mp_documents_keyboard.insert(go_mpdoc_programm)

go_mpdoc_documents = InlineKeyboardButton(text='Перечень документов для поступления', callback_data='go:mpdoc_documents')
mp_documents_keyboard.insert(go_mpdoc_documents)

go_mpdoc_terms = InlineKeyboardButton(text='Сроки подачи документов', callback_data='go:mpdoc_terms')
mp_documents_keyboard.insert(go_mpdoc_terms)

go_mpdoc_points = InlineKeyboardButton(text='Премиальные баллы по индивидуальным достижениям', callback_data='go:mpdoc_points')
mp_documents_keyboard.insert(go_mpdoc_points)

# Этапы зачисления бюджетной магистратуры (mp_stages - mps)

mp_stages_keyboard = InlineKeyboardMarkup(row_width=1)

go_mps_enrollment = InlineKeyboardButton(text='Зачисление', callback_data='go:mps_enrollment')
mp_stages_keyboard.insert(go_mps_enrollment)

go_mps_original = InlineKeyboardButton(text='Прием оригиналов документов', callback_data='go:mps_original')
mp_stages_keyboard.insert(go_mps_original)

go_mps_publication = InlineKeyboardButton(text='Публикация конкурсных списков', callback_data='go:mps_publication')
mp_stages_keyboard.insert(go_mps_publication)

go_mps_order = InlineKeyboardButton(text='Издание приказа о зачислении', callback_data='go:mps_order')
mp_stages_keyboard.insert(go_mps_order)


# Зачисление (mps_enrollmen - mpse)
mps_enrollment_keyboard = InlineKeyboardMarkup(row_width=1)

go_mpse_priority = InlineKeyboardButton(text='Этап приоритетного зачисления', callback_data='go:mpse_priority')
mps_enrollment_keyboard.insert(go_mpse_priority)

go_mpse_base = InlineKeyboardButton(text='Основной этап зачисления', callback_data='go:mpse_base')
mps_enrollment_keyboard.insert(go_mpse_base)



# Контакты
contact_keyboard = InlineKeyboardMarkup(row_width=1)

go_priem = InlineKeyboardButton(text='Приемная комиссия', callback_data='go:priem')
contact_keyboard.insert(go_priem)

go_faculty = InlineKeyboardButton(text='Факультет', callback_data='go:faculty')
contact_keyboard.insert(go_faculty)

cancel_button = InlineKeyboardButton(text='Назад', callback_data='go:cancel')
contact_keyboard.insert(cancel_button)


# Клавиатура "Наверх"
up_contact_keyboard = InlineKeyboardMarkup(row_width=1)

go_up = InlineKeyboardButton(text='Назад', callback_data='go:up')
up_contact_keyboard.insert(go_up)


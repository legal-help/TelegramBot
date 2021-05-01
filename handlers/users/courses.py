import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.choice_buttons import choice, b_ochnaya_keyboard, contact_keyboard, up_contact_keyboard, \
    magistratura_keyboard, m_budget_keyboard, m_pay_keyboard, mb_directions_keyboard, mb_documents_keyboard, \
    mb_stages_keyboard, mbs_enrollment_keyboard, mp_directions_keyboard, mp_documents_keyboard, mp_stages_keyboard
from loader import dp


@dp.message_handler(Command("start"))
async def show_courses(message: Message):
    await message.answer(text="Добрый день! Я бот-помощник абитуриента. Нажмите /course для выбора меню!")


@dp.message_handler(Command("course"))
async def show_courses(message: Message):
    await message.answer(text="Выберите направление:", reply_markup=choice)


@dp.callback_query_handler(text_contains='bakalavr')
async def go_in_bakalavr(call: CallbackQuery):
    await call.answer(cache_time=10)
    callback_data = call.data
    logging.info(f'call = {callback_data}')

    await call.message.answer('Вы выбрали Бакалавриат/специалитет. Продолжайте выбор.', reply_markup=b_ochnaya_keyboard)


@dp.callback_query_handler(text_contains='magistr')
async def go_in_magistr(call: CallbackQuery):
    await call.answer(cache_time=10)
    callback_data = call.data
    logging.info(f'call = {callback_data}')

    await call.message.answer('Вы выбрали Магистратуру. Продолжайте выбор.', reply_markup=magistratura_keyboard)


@dp.callback_query_handler(text_contains='b_budget')
async def go_budget(call: CallbackQuery):
    await call.answer(cache_time=10)
    callback_data = call.data
    logging.info(f'call = {callback_data}')
    text = 'good'

    await call.message.answer('Хорошо учиться на бюджете. Продолжайте выбор.')


@dp.callback_query_handler(text_contains='b_pay')
async def go_pay(call: CallbackQuery):
    await call.answer(cache_time=10)
    callback_data = call.data
    logging.info(f'call = {callback_data}')
    text = 'good'

    await call.message.answer('Хорошо учиться на платном отделении. Продолжайте выбор.')


@dp.callback_query_handler(text_contains='cancel')
async def cancel_button(call: CallbackQuery):
    await call.answer(cache_time=10)
    callback_data = call.data
    logging.info(f'call = {callback_data}')

    await call.message.answer('Вы перешли на уровень вверх. Продолжайте выбор.', reply_markup=choice)


# Магистратура
@dp.callback_query_handler(text_contains='m_budget')
async def go_in_m_budget(call: CallbackQuery):
    await call.answer(cache_time=10)
    callback_data = call.data
    logging.info(f'call = {callback_data}')

    await call.message.answer('Вы выбрали бюджетную основу. Продолжайте выбор.',
                              reply_markup=m_budget_keyboard)


@dp.callback_query_handler(text_contains='m_pay')
async def go_in_m_pay(call: CallbackQuery):
    await call.answer(cache_time=10)
    callback_data = call.data
    logging.info(f'call = {callback_data}')

    await call.message.answer('Вы выбрали платную основу. Продолжайте выбор.', reply_markup=m_pay_keyboard)


# Бюджетная магистратура

@dp.callback_query_handler(text_contains='mb_directions')
async def go_in_mb_directions(call: CallbackQuery):
    await call.answer(cache_time=10)
    callback_data = call.data
    logging.info(f'call = {callback_data}')

    await call.message.answer('Вы выбрали направления. Продолжайте выбор.', reply_markup=mb_directions_keyboard)

# Документы

@dp.callback_query_handler(text_contains='mb_documents')
async def go_in_mb_documents(call: CallbackQuery):
    await call.answer(cache_time=10)
    callback_data = call.data
    logging.info(f'call = {callback_data}')

    await call.message.answer('Вы выбрали документы. Продолжайте выбор.', reply_markup=mb_documents_keyboard)

# Этапы зачисления

@dp.callback_query_handler(text_contains='mb_stages')
async def go_in_mb_stages(call: CallbackQuery):
    await call.answer(cache_time=10)
    callback_data = call.data
    logging.info(f'call = {callback_data}')

    await call.message.answer('Вы выбрали этапы зачисления. Продолжайте выбор.', reply_markup=mb_stages_keyboard)

# Теория и практика конституционного правопользования

@dp.callback_query_handler(text_contains='mbd_tpp') # @dp.callback_query_handler(text_contains='md_tpp') # на две ветки
async def go_in_mbd_tpp(call: CallbackQuery):
    await call.answer(cache_time=10)
    callback_data = call.data
    logging.info(f'call = {callback_data}')

    await call.message.answer('''
    \tИнформация о направлении: 
    "Теория и практика конституционного правопользования".
    Преимуществом программ магистратуры в качестве второго высшего образования выступают возможность получения знаний
    по новой специализации и повышение своей конкурентоспособности на рынке труда.
    Форма обучения: очная
    Срок обучения: 2 года
    Выдаваемые документы: диплом государственного образца с присвоением степени магистра
    Программа аккредитована Ассоциацией юристов Россиии
    Отсрочка от армии на весь период обучения
    ''')

# Актуальные проблемы правозащитной и правоохранительной деятельности

@dp.callback_query_handler(text_contains='mbd_apppd') # на две ветки
async def go_in_mbd_apppd(call: CallbackQuery):
    await call.answer(cache_time=10)
    callback_data = call.data
    logging.info(f'call = {callback_data}')

    await call.message.answer('''
    Информация о направлении: 
    "Актуальные проблемы правозащитной и правоохранительной деятельности".
    Преимуществом программ магистратуры в качестве второго высшего образования выступают возможность получения знаний
    по новой специализации и повышение своей конкурентоспособности на рынке труда.
    Форма обучения: очная
    Срок обучения: 2 года
    Выдаваемые документы: диплом государственного образца с присвоением степени магистра
    Программа аккредитована Ассоциацией юристов Россиии
    Отсрочка от армии на весь период обучения
    ''')

# Документы
# Предметы
@dp.callback_query_handler(text_contains='mbdoc_subjects')
async def go_in_mbdoc_subjects(call: CallbackQuery):
    await call.answer(cache_time=10)
    callback_data = call.data
    logging.info(f'call = {callback_data}')

    await call.message.answer('Предметы для поступления: ')

# Программа вступительных испытаний

@dp.callback_query_handler(text_contains='mbdoc_programm')
async def go_in_mbdoc_programm(call: CallbackQuery):
    await call.answer(cache_time=10)
    callback_data = call.data
    logging.info(f'call = {callback_data}')

    await call.message.answer('Программа вступительных испытаний: ')

# Перечень документов для поступления
@dp.callback_query_handler(text_contains='mbdoc_documents')
async def go_in_mbdoc_documents(call: CallbackQuery):
    await call.answer(cache_time=10)
    callback_data = call.data
    logging.info(f'call = {callback_data}')

    await call.message.answer('Перечень документов для поступления: ')

# Сроки подачи документов
@dp.callback_query_handler(text_contains='mbdoc_terms')
async def go_in_mbdoc_terms(call: CallbackQuery):
    await call.answer(cache_time=10)
    callback_data = call.data
    logging.info(f'call = {callback_data}')

    await call.message.answer('Сроки подачи документов: ')

# Премиальные баллы по индивидуальным достижениям
@dp.callback_query_handler(text_contains='mbdoc_points')
async def go_in_mbdoc_points(call: CallbackQuery):
    await call.answer(cache_time=10)
    callback_data = call.data
    logging.info(f'call = {callback_data}')

    await call.message.answer('Премиальные баллы по индивидуальным достижениям: ')

# Этапы зачисления
# Зачисление
@dp.callback_query_handler(text_contains='mbs_enrollment')
async def go_in_mbs_enrollment(call: CallbackQuery):
    await call.answer(cache_time=10)
    callback_data = call.data
    logging.info(f'call = {callback_data}')

    await call.message.answer('''
    Выберите этап:
    ''', reply_markup=mbs_enrollment_keyboard)

# Прием оригиналов документов

@dp.callback_query_handler(text_contains='mbs_original')
async def go_in_mbs_original(call: CallbackQuery):
    await call.answer(cache_time=10)
    callback_data = call.data
    logging.info(f'call = {callback_data}')

    await call.message.answer('''
    Прием оригиналов документов: 
    ...
    ''')

# Публикация конкурсных списков
@dp.callback_query_handler(text_contains='mbs_publication')
async def go_in_mbs_publication(call: CallbackQuery):
    await call.answer(cache_time=10)
    callback_data = call.data
    logging.info(f'call = {callback_data}')

    await call.message.answer('Публикация конкурсных списков: ')

# Издание приказа о зачислении
@dp.callback_query_handler(text_contains='mbs_order')
async def go_in_mbs_order(call: CallbackQuery):
    await call.answer(cache_time=10)
    callback_data = call.data
    logging.info(f'call = {callback_data}')

    await call.message.answer('''
    Издание приказа о зачислении:  
    ...
    ''')

# Зачисление
# Этап приоритетного зачисления
@dp.callback_query_handler(text_contains='mbse_priority')
async def go_in_mbse_priority(call: CallbackQuery):
    await call.answer(cache_time=10)
    callback_data = call.data
    logging.info(f'call = {callback_data}')

    await call.message.answer('''
    Этап приоритетного зачисления:  
    ...
    ''')

# Основной этап зачисления
@dp.callback_query_handler(text_contains='mbse_base')
async def go_in_mbse_base(call: CallbackQuery):
    await call.answer(cache_time=10)
    callback_data = call.data
    logging.info(f'call = {callback_data}')

    await call.message.answer('''
    Основной этап зачисления:  
    ...
    ''')

# Платная магистратура

# Направления деятельности
@dp.callback_query_handler(text_contains='mp_directions')
async def go_in_mp_directions(call: CallbackQuery):
    await call.answer(cache_time=10)
    callback_data = call.data
    logging.info(f'call = {callback_data}')

    await call.message.answer('Вы выбрали направления. Продолжайте выбор.', reply_markup=mp_directions_keyboard)

# Документы

@dp.callback_query_handler(text_contains='mp_documents')
async def go_in_mp_documents(call: CallbackQuery):
    await call.answer(cache_time=10)
    callback_data = call.data
    logging.info(f'call = {callback_data}')

    await call.message.answer('Вы выбрали документы. Продолжайте выбор.', reply_markup=mp_documents_keyboard)

# Этапы зачисления

@dp.callback_query_handler(text_contains='mp_stages')
async def go_in_mp_stages(call: CallbackQuery):
    await call.answer(cache_time=10)
    callback_data = call.data
    logging.info(f'call = {callback_data}')

    await call.message.answer('Вы выбрали этапы зачисления. Продолжайте выбор.', reply_markup=mp_stages_keyboard)





# Контакты

@dp.callback_query_handler(text_contains='contact')
async def go_in_contact(call: CallbackQuery):
    await call.answer(cache_time=10)
    callback_data = call.data
    logging.info(f'call = {callback_data}')

    await call.message.answer('Контактная информация. Выберите:', reply_markup=contact_keyboard)


@dp.callback_query_handler(text_contains='priem')
async def go_priem(call: CallbackQuery):
    await call.answer(cache_time=10)
    callback_data = call.data
    logging.info(f'call = {callback_data}')
    # text = 'good'

    await call.message.answer('''
    \nКонтактная информация приемной комиссии:
    Телефон:
    +7 (4822) 32-15-14
    
    Подготовительные курсы:
    +7 (4822) 63-01-56
    +7 (4822) 32-28-72
    
    Сайт университета:
    http://university.tversu.ru
    
    Сайт приёмной комиссии:
    http://priem.tversu.ru
    
    Электронная почта приёмной комиссии:
    priem@tversu.ru
    
    Подача документов в электронно-цифровой форме  
    через личный кабинет поступающего: 
    https://abiturient.tversu.ru/
    (вход будет активен с 19 июня 2021 года).''', reply_markup=up_contact_keyboard)


@dp.callback_query_handler(text_contains='faculty')
async def go_faculty(call: CallbackQuery):
    await call.answer(cache_time=10)
    callback_data = call.data
    logging.info(f'call = {callback_data}')
    # text = 'good'

    await call.message.answer('''
    Контактная информация юридического факультета:
    Адрес: 170021, г. Тверь, 2-ая Грибоедова, д. 22
    
    Сайт факультета:
    https://law.tversu.ru

    Деканат направления подготовки 40.03.01 «Юриспруденция» (бакалавриат):
    +7 (4822) 52-94-22
    
    Деканат специальности 38.05.02 «Таможенное дело»:
    +7 (4822) 52-94-44
    
    Деканат направления подготовки 40.04.01 «Юриспруденция» (магистратура):
    +7 (4822) 52-12-26
    
    Email: law@tversu.ru''', reply_markup=up_contact_keyboard)


# Наверх

@dp.callback_query_handler(text_contains='up')
async def go_in_contact(call: CallbackQuery):
    await call.answer(cache_time=10)
    callback_data = call.data
    logging.info(f'call = {callback_data}')

    await call.message.answer('Назад', reply_markup=contact_keyboard)

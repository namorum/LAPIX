from yargy.pipelines import caseless_pipeline as gzt


INFO_HEADER = gzt([
    'Протокол технологической операции'
])

CONDITION_HEADER = gzt([
    'Условия окружающей среды при выполнении технологической операции'
])


TASK_HEADER = gzt([
    'Техническое задание на выполнение технологической операции'
])
OBJECT_HEADER = gzt([
    'Объект обработки'
])
MATERIAL_HEADER = gzt([
    'Материал для выполнения технологической операции'
])
REQS_HEADER = gzt([
    'Требования к результату операции'
])
DETAIL_HEADER = gzt([
    'Деталь'
])
SUBSTRATE_HEADER = gzt([
    'Подложка'
])
POWDER_HEADER = gzt([
    'Металлический порошок'
])
WIRE_HEADER = gzt([
    'Металлическая проволока'
])
DEFECTS_HEADER = gzt([
    'Дефекты наплавленного материала'
])
OTHER_FEATURES_HEADER = gzt([
    'Свойства'
])


# Заголовки, связанные с информацией об оборудовании
EQUIPMENT_HEADER = gzt([
    'Оборудование для выполнения технологической операции'
])
FEEDER_HEADER = gzt([
    'Узел подачи газопорошковой смеси',
    'Модуль подачи газопорошковой смеси'
])


# Заголовки, связанные с информацией о предварительной подготовки
PREPARE_HEADER = gzt([
    'Предварительная подготовка подложки',
    'Предварительная подготовка детали'
])
PRE_HEAT_HEADER = gzt([
    'Контролируемый нагрев'
])


# Заголовки, связанные с информацией о газовой среде
GAS_HEADER = gzt([
    'Газовая среда в рабочей камере'
])
SINGLE_GAS_HEADER = gzt([
    'Наполняющий газ'
])
GAS_MIX_HEADER = gzt([
    'Наполняющая газовая смесь'
])


# Заголовки, связанные с информацией о параметрах выполнения
PARAMS_HEADER = gzt([
    'Ключевые параметры выполнения ТО',
    'Ключевые параметры выполнения процесса',
    'Ключевые параметры выполнения ТО (процесса)'
])
HEAT_HEADER = gzt([
    'Сопутствующий нагрев объекта обработки'
])
LASER_HEADER = gzt([
    'Параметры лазерного излучения'
])
GAS_FEED_HEADER = gzt([
    'Параметры подачи технологических газов'
])
MATERIAL_FEED_HEADER = gzt([
    'Параметры подачи материала'
])
POSITIONING_HEADER = gzt([
    'Параметры перемещения и позиционирования рабочего инструмента относительно обрабатываемой поверхности'
])
MODE_HEADER = gzt([
    'Режим генерации лазерного излучения'
])
TRANSPORT_GAS_HEADER = gzt([
    'Параметры транспортирующего газа'
])
COMPRESSION_GAS_HEADER = gzt([
    'Параметры обжимающего газа'
])
POWDER_MIX_FEED_HEADER = gzt([
    'Композиция металлических порошков'
])
POWDER_FEED_HEADER = gzt([
    'Металлический порошок'
])
WIRE_FEED_HEADER = gzt([
    'Металлическая проволока'
])
TIMED_POWER_HEADER = gzt([
    'Значение мощности изменялось в процессе перемещения лазерного пучка по обрабатываемой поверхности'
])
LAYERED_POWER_HEADER = gzt([
    'Значение мощности по слоям'
])
SINGLE_SHIELD_GAS_HEADER = gzt([
    'Параметры защитного газа'
])
SHIELD_GAS_MIX_HEADER = gzt([
    'Параметры защитной газовой смеси'
])
HORIZONTAL_SHIFT_HEADER = gzt([
    'Горизонтальное (x, y) смещение между слоями'
])
WELD_FOCUS_HEADER = gzt([
    'Положение фокуса излучения относительно обрабатываемой поверхности'
])
MELT_FOCUS_HEADER = gzt([
    'Взаимное расположение центров фокусов ГПС и лазерного излучения'
])
MELT_FOCUS_AXIS_HEADER = gzt([
    'По оси X',
    'По оси Y'
])


# Заголовки, связанные с информацией о контролируемом охлаждении
COOL_HEADER = gzt([
    'Контролируемое охлаждение'
])


# Заголовки, связанные с информацией о результате выполнения
RESULT_HEADER = gzt([
    'Результат выполнения технологической операции'
])
RESULT_DESC_HEADER = gzt([
    'Описание результата'
])
RESULT_GEOMETRY_HEADER = gzt([
    'Геометрические характеристики'
])
RESULT_ELEMENTS_HEADER = gzt([
    'Элементный состав'
])
RESULT_MICROSTRUCTURE_HEADER = gzt([
    'Микроструктура'
])
RESULT_DEFECTS_HEADER = gzt([
    'Дефекты наплавленного материала'
])
DESC_HEADER = gzt([
    'Описание'
])
EVAL_HEADER = gzt([
    'Оценка'
])


# Заголовки, связанные с общими правилами
GEOMETRY_HEADER = gzt([
    "Геометрические характеристики"
])
ELEMENTS_HEADER = gzt([
    "Элементный состав",
    "Элементный (химический) состав",
    "Химический состав"
])
MICROSTRUCTURE_HEADER = gzt([
    "Микроструктура"
])
GRANULOMETRY_HEADER = gzt([
    "Размер частиц",
    "Гранулометрический состав"
])


# Единицы измерения значений
UNIT = gzt([
    "кПа",
    "Па",
    "мм рт. ст.",
    "K",
    "К/мин",
    "н.л/мин",
    "°C",
    "кг",
    "%",
    "Вт",
    "кВт",
    "Вт/см2",
    "г/с",
    "г/см3",
    "г/мин",
    "об/мин",
    "мм/с",
    "л/мин",
    "н.л./мин",
    "МПа",
    "ГПа",
    "бар",
    "м/с",
    "рад/с",
    "мрад/с",
    "мм",
    "см",
    "м",
    "°",
    "рад",
    "%",
    "<не задано>"
])


# Напименования заранее определённых свойств
NAME = gzt([
    "Номер протокола технологической операции",
    "Срок выполнения технологической операции",
    "Цель выполнения технологической операции",
    "Место выполнения технологической операции",
    "Температура окружающей среды",
    "Влажность окружающей среды",
    "Относительная влажность",
    "Атмосферное давление",
    "Материал основы",
    "Материал рабочей поверхности",
    "Материал",
    "Длина",
    "Ширина",
    "Высота",
    "Масса",
    "Насыпная плотность",
    "Сыпучесть",
    "Технологический лазер",
    "Устройство для перемещения оптической головы относительно обрабатываемой поверхности",
    "Лазерная оптическая голова",
    "Порошковый питатель",
    "Режим генерации лазерного излучения",
    "Мощность",
    "Диаметр пятна лазерного пучка на обрабатываемой поверхности",
    "Диаметр пучка на обрабатываемой поверхности",
    "Диаметр",
    "Плотность мощности",
    "Массовый расход порошка",
    "Массовый расход",
    "Количество оборотов дозирующего диска порошкового питателя",
    "Скорость подачи проволоки",
    "Скорость подачи",
    "Газ",
    "Объемный расход",
    "Объёмный расход",
    "Давление",
    "Температура",
    "Объемная доля",
    "Объёмная доля",
    "Линейная скорость перемещения сфокусированного лазерного пучка по обрабатываемой поверхности",
    "Скорость перемещения сфокусированного лазерного пучка по обрабатываемой поверхности",
    "Угловая скорость вращения устройства позиционирования",
    "Фокусное расстояние фокусирующей линзы",
    "Расстояние от места фокусировки лазерного излучения до обрабатываемой поверхности",
    "Расстояние от нижней поверхности сопла оптической головы до обрабатываемой поверхности",
    "Величина вертикального (z) смещения оптической головы относительно поверхности предварительно наплавленного слоя",
    "Шаг смещения центра сфокусированного лазерного пучка относительно центра предварительно созданного валика (трека)",
    "Линейная скорость холостого перемещения оптической головы относительно обрабатываемой поверхности",
    "Скорость холостого перемещения оптической головы относительно обрабатываемой поверхности",
    "Угол наклона оптической головы",
    "Положение фокуса излучения относительно обрабатываемой поверхности",
    "Материал подложки",
    "Начальная температура обрабатываемой поверхности",
    "Предварительная обработка поверхности",
    "Обработка поверхности",
    "Изображение результата операции",
    "Постобработка",
    "Форма частиц",
    "Скорость",
    "частота модуляции",
    "длительность импульса",
    "частота следования импульсов",
    "Плотность мощности",
    "Тип подачи металлического порошкового материала в зону обработки",
    "Угол конуса",
    "Ширина зазора коаксиальной щели",
    "Оценка результата",
    "Комментарий оператора"
])

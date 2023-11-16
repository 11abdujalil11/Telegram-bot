from aiogram.dispatcher.filters.state import State, StatesGroup


class Condition(StatesGroup):
    Language = State()
    Uz_Phone_Number = State()
    Uz_PhonePricing_AirpodsPricing_ChangeLanugage = State()
    Uz_Phone_Models = State()
    Uz_Phone_Series = State()

    Uz_iPhone_SE_2016_Battery = State()
    Uz_iPhone_SE_2016_DocBox = State()
    Uz_iPhone_SE_2016_Colors = State()
    Uz_iPhone_SE_2016_Storage = State()
    Uz_iPhone_SE_2016_Created_Place = State()
    Uz_iPhone_SE_2016_Injury = State()
    Uz_iPhone_SE_2016_Damage = State()

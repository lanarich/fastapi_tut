from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram import F
from keyboards.inline import place_kb
from aiogram import Router
import httpx
import json
from state.prediction import com3, com4, com5, com6

router_command = Router()

base_url = "http://fastapi_service:5555"


@router_command.message(F.text == "🐕 Выбрать команду 🐈‍⬛")
async def start_predict_items(message: Message):
    await message.answer(f'Нажмите на кнопку ниже',reply_markup=place_kb())

@router_command.callback_query(F.data.startswith('set'))
async def select_mark(call: CallbackQuery, state: FSMContext):
    com = call.data.split(':')[1]
    
    if com == "1":
        response_get = httpx.get(f"{base_url}/")
        answer = json.dumps(response_get.json(), indent=1)     
        await call.message.answer(answer, reply_markup=place_kb())
    elif com == "2":
        response_get = httpx.post(f"{base_url}/post")
        answer = json.dumps(response_get.json(), indent=1)     
        await call.message.answer(answer, reply_markup=place_kb())
        
    elif com == "3":
        await call.message.answer(f'Введите одну из 3-х пород:\n'
                              '1. terrier\n'
                              '2. bulldog\n'
                              '3. dalmatian\n')
        await state.set_state(com3.post_1)
        
        @router_command.message(com3.post_1)
        async def get_dog_2(message: Message):
            response_get = httpx.get(f"{base_url}/dog?kind={message.text}")
            answer = json.dumps(response_get.json(), indent=1)     
            await message.answer(answer, reply_markup=place_kb())
        
        
            
    elif com == "4":
        await call.message.answer(f'Введите данные новой собаки в формате <b>json</b> как в примере ниже:\n\n'
                          '{\n'
                          '    "name": "string",\n'
                          '    "pk": 0,\n'
                          '    "kind": "terrier"\n'
                          '}\n')
        await state.set_state(com4.post_1)
        
        @router_command.message(com4.post_1)
        async def post_dog(message: Message):
            data_input = message.text
            response_post = httpx.post(f"{base_url}/dog", json = json.loads(data_input))
            await message.answer(f'Ответ успешно записан!', reply_markup=place_kb())
        
        
           
    elif com == "5":
        await call.message.answer(f'Введите <b>pk</b> собаки ниже')
        await state.set_state(com5.post_1)
        
        @router_command.message(com5.post_1)
        async def get_dog_pk(message: Message):
            response_get = httpx.get(f"{base_url}/dog/{message.text}")
            answer = json.dumps(response_get.json(), indent=1)     
            await message.answer(answer, reply_markup=place_kb())
        
        
    elif com == "6":
        await call.message.answer(f'Введите <b>pk</b> собаки, информацию о которой нужно обновить')
        await state.set_state(com6.post_1)
        
        @router_command.message(com6.post_1)
        async def patch_dog_pk(message: Message, state: FSMContext):
            await state.update_data(post_1 = message.text)
            await message.answer(f'Введите обновленные данные собаки в формате <b>json</b> как в примере ниже:\n\n'
                          '{\n'
                          '    "name": "string",\n'
                          '    "pk": 0,\n'
                          '    "kind": "terrier"\n'
                          '}\n')
            await state.set_state(com6.post_2)
        
        
        @router_command.message(com6.post_2)
        async def patch_dog_info(message: Message, state: FSMContext):
            await state.update_data(post_2 = message.text)
            data = await state.get_data()
            response_get = httpx.patch(f"{base_url}/dog/{data['post_1']}", json = json.loads(data['post_2']))
            await message.answer(f'Данные успешно обновлены!', reply_markup=place_kb())
    
    
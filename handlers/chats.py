from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from keyboards.default.start import courses, user_main_menu
from states.user import RegisterState

router = Router()


@router.message(F.text == "🎓 Course")
async def chat_course_handler(message: types.Message, state: FSMContext):
    text = "Information about all our courses"

    await message.answer(text=text, reply_markup=courses)
    await state.set_state(RegisterState.courses)


@router.message(RegisterState.courses, F.text == "🐍 Backend (Python)")
async def chat_backend_handler(message: types.Message, state: FSMContext):
    text = ("""🐍 Backend Development (Python Backend)

    👩‍💻 What you will learn:
        Python fundamentals
        Django / FastAPI
        REST APIs
        Databases (PostgreSQL, SQLite)
        Authentication & authorization
        Git, deployment basics
        
    Duration:⏳ 6–7 months
        
    Result: You will be able to build server-side logic, APIs, and full backend systems."""
)
    await message.answer(text=text, reply_markup=courses)
    await state.set_state(RegisterState.courses)


@router.message(RegisterState.courses, F.text == "💻Frontend Development")
async def chat_backend_handler(message: types.Message, state: FSMContext):
    text = ("""💻Frontend Development
            
    👩‍💻 What you will learn:
        HTML, CSS, JavaScript
        Responsive web design
        Modern frameworks (React basics)
        Working with APIs
        Git & GitHub
         
    Duration: ⏳ 5–6 months
        
    Result: You will be able to build modern, interactive websites and user interfaces."""
            )

    await message.answer(text=text, reply_markup=courses)
    await state.set_state(RegisterState.courses)


@router.message(RegisterState.courses, F.text == "🧩 UI/UX & Graphic Design")
async def chat_backend_handler(message: types.Message, state: FSMContext):
    text = ("""🧩 UI/UX & Graphic Design"

    👩‍💻 What you will learn:
        Design principles & color theory
        UI/UX basics
        Figma
        Adobe Photoshop & Illustrator
        Web & mobile design layouts
        Branding basics
        
    Duration: ⏳ 4–5 months
        
    Result: You will be able to design modern interfaces, logos, and digital products."""
            )
    await message.answer(text=text, reply_markup=courses)
    await state.set_state(RegisterState.courses)


@router.message(RegisterState.courses, F.text == "📊 Digital Marketing")
async def chat_backend_handler(message: types.Message, state: FSMContext):
    text =( """📊 Digital Marketing

    👩‍💻 What you will learn:
        SMM (Instagram, Telegram, Facebook)
        Content creation
        Targeted advertising (Meta Ads, Google Ads)
        SEO basics
        Analytics & strategy
        
    Duration: ⏳ 3–4 months
        
    Result: You will be able to promote brands and products online effectively."""
            )
    await message.answer(text=text, reply_markup=courses)
    await state.set_state(RegisterState.courses)


@router.message(RegisterState.courses, F.text == "⬅️ Back")
async def chat_backend_handler(message: types.Message, state: FSMContext):
    text = "⬅️ Back"
    await message.answer(text=text, reply_markup=user_main_menu)
    await state.clear()


@router.message(F.text == "☎️ Contacts")
async def chat_contacts_handler(message: types.Message):
    text = """📍 Najot Ta’lim filiallari va nomerlari

--Najot Ta'lim Chimboy filiali
📌 Manzil: Chimboy, Toshkent
☎️ Tel: +998 99 081-5121 (filial telefon)
📚 Kurslar: dasturlash, dizayn, marketing va boshqalar

Najot Ta'lim Chilonzor Filial
📌 Manzil: Qatortol ko‘chasi, 1B, Chilonzor, Toshkent
☎️ Tel: +998 78 888-98-88 (asosiy raqam)
📌 Filial haqida ma’lumot: kurslar, konsultatsiya, sertifikatlar

Najot Ta’lim Markazi (Toshkent)
📌 Asosiy markaz: Toshkent
☎️ Tel: +998 78 888-98-88
📚 Dasturlash, dizayn, marketing va boshqa kurslar

Najot Ta’lim — Xadra filiali
📌 Manzil: Sebzar ko‘chasi, 1, Shayxontohur, Toshkent
☎️ Tel: +998 78 888-98-88
✨ Kurslar va konsultatsiya mavjud

Najot Ta’lim — Samarqand filiali
📌 Manzil: Rudaki ko‘chasi, 225, Samarqand
☎️ Tel: +998 78 888-98-88 (asosiy raqam bo‘lishi ehtimoli yuqori)

Najot Ta’lim — Farg‘ona filiali
📌 Manzil: Kuvasoy ko‘chasi, Farg‘ona
☎️ Tel: +998 78 888-98-88 (bir xil raqam bo‘ladi)

Najot Ta’lim — Urganch (Xorazm) filiali
📌 Manzil: Al-Xorazmiy ko‘chasi, 68B, Urganch
☎️ Tel: +998 78 888-98-88 (bir xil raqam bo‘lishi mumkin)"""

    await message.answer(text=text, reply_markup=user_main_menu)
from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from keyboards.default.start import courses, user_main_menu
from states.user import RegisterState

router = Router()


@router.message(F.text == "🎓 Course")
async def chat_course_handler(message: types.Message, state: FSMContext,_):
    text = _("Information about all our courses")

    await message.answer(text=text, reply_markup=await courses(_))
    await state.set_state(RegisterState.courses)


@router.message(RegisterState.courses, F.text == "🐍 Backend (Python)")
async def chat_backend_handler(message: types.Message, state: FSMContext,_):
    text = _("""🐍 Backend Development (Python Backend)

    👩‍💻 What you will learn:
        Python fundamentals
        Django / FastAPI
        REST APIs
        Databases (PostgresSQL, SQLite)
        Authentication & authorization
        Git, deployment basics
        
    Duration:⏳ 6–7 months
        
    Result: You will be able to build server-side logic, APIs, and full backend systems."""
)
    await message.answer(text=text, reply_markup=await courses(_))
    await state.set_state(RegisterState.courses)


@router.message(RegisterState.courses, F.text == "💻Frontend Development")
async def chat_backend_handler(message: types.Message, state: FSMContext,_):
    text = _("""💻Frontend Development
            
    👩‍💻 What you will learn:
        HTML, CSS, JavaScript
        Responsive web design
        Modern frameworks (React basics)
        Working with APIs
        Git & GitHub
         
    Duration: ⏳ 5–6 months
        
    Result: You will be able to build modern, interactive websites and user interfaces."""
            )

    await message.answer(text=text, reply_markup=await courses(_))
    await state.set_state(RegisterState.courses)


@router.message(RegisterState.courses, F.text == "🧩 UI/UX & Graphic Design")
async def chat_backend_handler(message: types.Message, state: FSMContext,_):
    text = _("""🧩 UI/UX & Graphic Design"

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
    await message.answer(text=text, reply_markup=await courses(_))
    await state.set_state(RegisterState.courses)


@router.message(RegisterState.courses, F.text == "📊 Digital Marketing")
async def chat_backend_handler(message: types.Message, state: FSMContext,_):
    text =_( """📊 Digital Marketing

    👩‍💻 What you will learn:
        SMM (Instagram, Telegram, Facebook)
        Content creation
        Targeted advertising (Meta Ads, Google Ads)
        SEO basics
        Analytics & strategy
        
    Duration: ⏳ 3–4 months
        
    Result: You will be able to promote brands and products online effectively."""
            )
    await message.answer(text=text, reply_markup=await courses(_))
    await state.set_state(RegisterState.courses)


@router.message(RegisterState.courses, F.text == "⬅️ Back")
async def chat_backend_handler(message: types.Message, state: FSMContext,_):
    text = _("⬅️ Back")
    await message.answer(text=text, reply_markup=await user_main_menu(_))
    await state.clear()


@router.message(F.text == "☎️ Contacts")
async def chat_contacts_handler(message: types.Message,_):
    text = _("""📍 Najot Ta’lim branches and contact numbers

--Najot Ta'lim Chimboy Branch
📌 Address: Chimboy, Tashkent
☎️ Phone: +998 99 081-5121 (branch phone)
📚 Courses: programming, design, marketing, and others

Najot Ta'lim Chilonzor Branch
📌 Address: Qatortol street, 1B, Chilonzor, Tashkent
☎️ Phone: +998 78 888-98-88 (main number)
📌 Branch info: courses, consultations, certificates

Najot Ta’lim Center (Tashkent)
📌 Main center: Tashkent
☎️ Phone: +998 78 888-98-88
📚 Programming, design, marketing, and other courses

Najot Ta’lim — Xadra Branch
📌 Address: Sebzar street, 1, Shaykhontohur, Tashkent
☎️ Phone: +998 78 888-98-88
✨ Courses and consultations available

Najot Ta’lim — Samarkand Branch
📌 Address: Rudaki street, 225, Samarkand
☎️ Phone: +998 78 888-98-88 (likely main number)

Najot Ta’lim — Fergana Branch
📌 Address: Kuvasoy street, Fergana
☎️ Phone: +998 78 888-98-88 (same number)

Najot Ta’lim — Urgench (Khorezm) Branch
📌 Address: Al-Khorezmi street, 68B, Urgench
☎️ Phone: +998 78 888-98-88 (possibly same number)
""")

    await message.answer(text=text, reply_markup=await user_main_menu(_))
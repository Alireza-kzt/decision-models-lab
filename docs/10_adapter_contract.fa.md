# قرارداد adapter

## حداقل قرارداد
`predict(state, question, options) -> dict[option_id, probability]` برای یک choice تک‌برچسبی. شناسه‌ها معنایی و پایدارند؛ ترتیب نمایش ویژگی جداست. هیچ adapter نباید label یا split را به مدل بدهد.

## الزامات
پاسخ باید دقیقاً گزینه‌های ورودی را پوشش دهد؛ احتمال finite و در بازهٔ صفر تا یک باشد؛ جمع با tolerance مشخص یک شود. به جای renormalize مخفی، خطا گزارش شود. raw response و request بدون secret، model revision، retryها، timestamp و هزینه ذخیره شوند. خطای شبکه، refusal و invalid schema را صفرِ احتمالات فرض نکنید.

## fixtureها
choice دودویی و چندکلاسه، candidateهای هم‌معنا، ترتیب معکوس، ورودی بلند، نویسهٔ غیرلاتین، state خالی، schema تکراری، گزینهٔ گمشده، null/NaN، HTTP failure و پاسخ جزئی. برای API تست قرارداد باید جدا از تست علمی باشد.

## پشتیبانی اجرایی امروز
فقط UniformAdapter غیرهوشمند برای smoke و ارزیابی JSONL ذخیره‌شده وجود دارد. تمام adapterهای Jev، Clef، pplx، GLiNER و بقیه در registry برچسب not_implemented دارند. نمی‌توان نام مدل را به runner داد و انتظار دانلود یا اجرای آن داشت.

## افزودن implementation واقعی
ابتدا منبع API/کد جاری را بررسی و pin کنید. یک adapter کوچک بسازید؛ capabilityها را صریح اعلام کنید؛ unsupported type خطا بدهد. fixtureهای sanitised ذخیره کنید و unittest بنویسید. سپس یک pilot ازپیش‌ثبت‌شده اجرا کنید. استفاده از API key و هزینه باید آگاهانه فعال شود، نه به‌طور پیش‌فرض.

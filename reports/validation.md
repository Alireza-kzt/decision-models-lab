# گزارش اعتبارسنجی زیرساخت

تاریخ تدوین بسته: 2026-10-07. **این گزارش نتیجهٔ اجرای مدل واقعی نیست.**

## اجراهای واقعی این محیط
- `python -m unittest discover -s tests -v`: **29 tests passed**.
- `python -m decision_lab validate`: registryها، کارت‌ها، ارجاع‌ها و fixtureها معتبرند.
- `python -m decision_lab smoke`: اجرای موفق uniform demo روی شش نمونهٔ دست‌نویس.
- `python -m decision_lab evaluate`: اجرای موفق روی احتمال‌های دست‌نویس؛ inference واقعی نیست.
- `python scripts/publish_private.py`: dry-run اولیه موفق بود؛ این آیتم صرفاً آزمون helper است. Push واقعی بعداً، پس از ساخت repository توسط مالک، از طریق اتصال GitHub انجام شد.

خروجی کامل تست‌ها: [unit-tests.txt](unit-tests.txt). نتیجهٔ validator: [registry-validation.json](registry-validation.json). خروجی dry-run: [publish-dry-run.txt](publish-dry-run.txt).

## دامنهٔ پوشش
احتمال NaN/Infinity/رشته/boolean، جمع نامعتبر، label خارج از schema، شناسهٔ تکراری/گمشده/اضافی، group leakage، split مخلوط، تعداد گزینهٔ ناسازگار، tie-break ثابت، Brier/NLL/ECE با پاسخ محاسبه‌شده، حفظ run شکست‌خورده و امتناع از overwrite بررسی شده‌اند.

## محیط
Python: `3.13.5`. سیستم: `Linux`، معماری: `x86_64`. هسته وابستگی third-party ندارد.

## چیزهایی که تست نشده‌اند
ساخت repository توسط ابزار محلی، اجرای CI در GitHub، اجرای ویندوز، مدل‌های GPU، APIهای ارائه‌دهنده، training، bootstrap آماری و پروتکل‌های E001–E005. انتقال فایل‌ها به repository خصوصی بعداً از طریق GitHub API انجام شد، اما این انتقال آزمون علمی مدل نیست. اسکریپت انتشار برای bootstrap مستقل با Git/GitHub CLI نگه داشته شده است؛ repository موجود در این تحویل از مسیر اتصال GitHub نوشته شد.

## نتیجه
هستهٔ آفلاین و اسناد برای شروع مطالعه/آزمایش آماده‌اند. **صفر run واقعی برای Jev یا رقبا، صفر fine-tune و صفر ادعای تجربی آمادهٔ مقاله.**

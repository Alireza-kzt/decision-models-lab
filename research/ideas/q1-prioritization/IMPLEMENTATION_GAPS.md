# فاصلهٔ مستندات تا اجرای واقعی

[فهرست رتبه‌ها](README.md) · [پروتکل](PROTOCOL.md) · [اعتبارسنجی انجام‌شده](VALIDATION.md)

رتبهٔ بالای امکان اجرا به معنی آماده بودن کد پایلوت نیست. موارد این فایل backlog فنی‌اند؛ در این تغییر پیاده‌سازی نشده‌اند. مبنای بررسی کد: `59f20dc9ed51acf5ad2058c43c57bdfc22b2df5d`.

## محدودیت مهم C002/C001

در [schema.py](../../../decision_lab/schema.py)، تابع `load_examples(..., evaluation=True)` صریحاً یک `fixed option-ID universe` می‌خواهد. [metrics.py](../../../decision_lab/metrics.py) نیز labels را از نمونهٔ نخست می‌گیرد و تفاوت مجموعهٔ گزینه‌ها را رد می‌کند. [test_schema.py](../../../tests/test_schema.py) با `test_variable_options_rejected` این قرارداد فعلی را تثبیت کرده است.

بنابراین مخلوط کردن نمونه‌های با تعداد/معنای متفاوت گزینه در یک فایل، **اکنون قابلیت پشتیبانی‌شده نیست**. حذف یک validation بدون بازطراحی metricها، راه‌حل صحیح نیست.

### تغییرات پیشنهادی قبل از P1/P3

یک نسخهٔ تازهٔ schema با option IDs معنایی per-item، شناسهٔ نمونهٔ مادر، خانوادهٔ schema، نوع transformation و در صورت وجود mapping رویدادها تعریف شود. فیلدهای اضافه را به schema سخت‌گیر فعلی تحمیل نکنید. فقط synthetic دارای oracle، فیلد توزیع مرجع را بگیرد؛ دادهٔ واقعی تک‌برچسبی ground-truth probability ندارد.

NLL و Brier ابتدا per-item و سپس با وزن گروه/خانوادهٔ اعلام‌شده تجمیع شوند. مقایسهٔ روش‌ها باید بر همان موارد و cardinality یکسان باشد؛ تفاوت NLL خام میان مسائل ذاتاً با تعداد گزینهٔ متفاوت را خودکار به خرابی calibration نسبت ندهید. baseline uniform یا تحلیل per-cardinality می‌تواند مقایسه را روشن کند. Macro-F1 جهانی روی option IDهای نامرتبط وظایف معنا ندارد؛ فقط در یک فضای برچسب مشترک محاسبه شود.

قرارداد clipping فعلی NLL برابر `1e-15` است و در خروجی metric ثبت می‌شود؛ برای مطالعهٔ جدید باید اثر آن و قرارداد یکسان بین روش‌ها روشن باشد. Tie-breaking فعلی semantic-ID lexicographic است؛ اگر IDs صرفاً شمارهٔ slot باشند، تضمین تصمیم زیر permutation از بین می‌رود. ID معنایی و slot را جدا کنید.

آزمون‌های لازم: جمع احتمال و اعتبار label برای هر item، نبود نشت group بین splitها، تطبیق mapping رویداد بعد از permutation/merge، محاسبهٔ دستی NLL/Brier برای Kهای مختلف، عدم شمارش variantها به‌عنوان نمونهٔ مستقل، و backward compatibility با fixtureهای قبلی.

## محدودیت مهم C006

metric فعلی selective risk را برای یک threshold حساب می‌کند، اما **statistical intervals در آن implemented نیست**. replay چندمدلی، policyِ کامل fallback/abstain، certification با family ثابت، ماتریس گروه‌ها و bootstrap گروهی هنوز توسعهٔ لازم دارند. خروجی یک threshold ساده را گواهی ریسک ننامید.

## زیرساخت عمومی

adapter زنده، checkpoint pinned، دفتر هزینهٔ GPU/API، مجوز دادهٔ تأییدشده و benchmark واقعی هنوز نداریم. تقدم پیشنهادی مهندسی: قرارداد داده → evaluator و تست‌ها → یک adapter کوچک → ذخیرهٔ prediction/version → baseline ساده → پایلوت. آموزش MoE، diffusion یا drafter تا قبل از عبور از این مراحل اولویت ندارد.

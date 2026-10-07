# وضعیت تحویل

تاریخ به‌روزرسانی: 2026-10-07.

مخزن خصوصی زیر توسط مالک در GitHub ایجاد شد و سپس محتوای کامل این آزمایشگاه از طریق اتصال GitHub همین نشست روی شاخهٔ `main` قرار گرفت:

- Repository: `Alireza-kzt/decision-models-lab`
- Visibility: `private`
- Default branch: `main`
- Initial GitHub commit حفظ شده و commit آزمایشگاه به‌صورت فرزند آن ثبت می‌شود؛ force-push مخرب انجام نشده است.

## وضعیت محتوا
تمام فایل‌های tracked نسخهٔ محلی اعتبارسنجی‌شده به GitHub منتقل می‌شوند. هیچ checkpoint، دیتاست خصوصی، secret یا فایل PDF شخص ثالث در این تحویل اضافه نشده است.

## روش انتقال
انتقال با GitHub repository write API انجام شد؛ نه با token کاربر در فایل‌ها و نه با انتشار عمومی. README اولیهٔ یک‌خطی GitHub با README کامل آزمایشگاه جایگزین می‌شود و تاریخچهٔ آن باقی می‌ماند.

## نکته دربارهٔ اسکریپت انتشار
`scripts/publish_private.py` ابزار bootstrap برای حالتی است که repository هنوز وجود ندارد. بعد از این تحویل، برای همین نام repository نباید از حالت `--execute` آن جهت ساخت مجدد استفاده شود. تغییرات بعدی باید به همین repository موجود commit/push شوند.

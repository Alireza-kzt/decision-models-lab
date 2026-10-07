# مدل Clef / Clef-Flash

**نوع:** `native_decision_weights` · **سازنده:** Cloudflare · **بررسی:** 2026-10-07

## آنچه منبع می‌گوید
Cloudflare برای Clef و نسخهٔ Flash به‌ترتیب Qwen3.8-27B و Qwen3.5-9B، مسیریابی شواهد گزینه‌ها و توجه بین فیلدها را گزارش می‌کند. آموزش شامل head، LoRA و هدف‌های تصمیم و کالیبراسیون است.

## وضعیت دسترسی و ارجاع
وزن: `reported_available`؛ کد: `reported_available`؛ مجوز: Apache-2.0 reported.
این‌ها گزارش منابع هستند، نه تأیید اجرای محلی یا ممیزی حقوقی.

مرجع پژوهشی: پیپر اختصاصی در منابع بررسی‌شده تأیید نشده؛ نبود قطعی مقاله ادعا نمی‌شود.

## احتیاط و سؤال پژوهشی
وجود توجه مشترک بین فیلدها از پیش گزارش شده؛ ایدهٔ صرفاً اضافه‌کردن joint head نوآوری اثبات‌شده نیست. نسخه و مجوز دقیق هر checkpoint باید پیش از اجرا قفل شود.

## گام بعدی این آزمایشگاه
نسخهٔ تغییرناپذیر و شرایط استفاده ثبت شود؛ سپس fixtureهای قرارداد خروجی، ترتیب گزینه‌ها و ورودی نامعتبر اجرا شوند. adapter این مدل هنوز پیاده‌سازی نشده و هیچ run واقعی برای آن نداریم.

## منابع مستقیم
- [S002: Introducing Clef: our open-source decision models, and new RL fine-tuning platform](https://blog.cloudflare.com/clef-decision-models/)
- [S003: Cloudflare/clef](https://huggingface.co/Cloudflare/clef)

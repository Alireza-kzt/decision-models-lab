# ایدهٔ H005 — cascade با کنترل ریسک در تغییر دامنه

وضعیت: **فرضیه / اجرا نشده / novelty تأیید نشده**. هیچ‌یک هدف نهایی پروژه نیست.

## سؤال
آیا یک cascade با معیار عدم‌قطعیت می‌تواند در domain shift هزینه را پایین نگه دارد و ریسک را مهار کند؟

## فرضیهٔ ابطال‌پذیر
gate آگاه از shift شاید نسبت به max-confidence routing پوشش/ریسک بهتری در توزیع تازه داشته باشد.

## نزدیک‌ترین پیشینه و ریسک تکراری بودن
cascade در P003 و adaptive compute در GLiDE پیشینه دارد. ارزان‌کردن با یک مدل کوچک در ابتدای مسیر به‌تنهایی novelty ندارد.

## کوچک‌ترین آزمایش مفید
classifier ارزان، مدل تصمیم باز کوچک و یک مدل قوی‌تر. کنترل‌ها: تک‌مدل، gate تصادفی، gate confidence و روش پیشنهادی. هزینهٔ teacher، timeouts و retry در کل pipeline ثبت شود.

## معیار و کنترل
quality-cost frontier، risk-coverage، escalation rate و end-to-end p95 با concurrency ثابت؛ به‌صورت ID و OOD جدا.

## چه نتیجه‌ای ما را منصرف می‌کند؟
صرفه‌جویی فقط از utilization غیرمنصفانه یا سرویس/سخت‌افزار متفاوت باشد؛ بهبود در risk از رد همهٔ نمونه‌های سخت حاصل شود.

## وابستگی قبل از اجرا
انتخاب dataset با مجوز روشن، pin کردن checkpoint، نوشتن adapter و preregistration. هیچ GPU یا مبلغی در این ایده تصویب نشده است. بعد از pilot، effect size عملی و سقف trialها مشخص شود؛ test برای انتخاب آن‌ها استفاده نشود.

## شواهد و کار باز
[P003](../../catalog/papers/P003.md); [P006](../../catalog/papers/P006.md); [glide](../../catalog/models/glide.md); [laya](../../catalog/models/laya.md)

**شواهد محلی:** ندارد. **تصمیم:** باز. نتیجهٔ منفی نیز باید همراه با علت حفظ شود.

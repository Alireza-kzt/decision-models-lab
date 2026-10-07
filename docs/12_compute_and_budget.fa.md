# محاسبه و بودجه

هدف این سند برنامه‌ریزی است، نه توصیهٔ خرید GPU. اندازهٔ پایه، trainable parameters، context، تعداد گزینه، batch و optimizer را پیش از برآورد مشخص کنید.

حافظهٔ وزن خام تقریباً برابر است با:

\[
M_{weights}\approx N_{params}\times b/8\quad\text{bytes}.
\]

این مقدار **کل VRAM لازم نیست**: activation، workspace، state optimizer، گرادیان، cache، سربار runtime و fragmentation اضافه‌اند. LoRA تعداد پارامترهای قابل آموزش را کم می‌کند ولی همهٔ هزینهٔ نگهداری backbone را حذف نمی‌کند. Quantization هم معیار کیفیت را تغییر می‌دهد و باید در ablation ثبت شود.

## ترتیب پیشنهادی
اول تست‌های CPU و fixture؛ سپس یک batch برای سنجش peak memory؛ بعد pilot با تعداد نمونهٔ محدود؛ تنها پس از آن انتخاب تعداد seed و sweep. قیمت GPU و API باید در روز اجرا از ارائه‌دهنده ثبت شود؛ قیمت یا زمان ثابت برای مدل‌های این فهرست فرض نشده است.

## فرم مجوز اجرا
مدل/revision، داده و اجازهٔ ارسال، سخت‌افزار/ارائه‌دهنده، سقف مبلغ، حداکثر request یا step، deadline توقف job، محل ذخیره، رفتار در خطا و مسئول خاموش‌کردن منابع. هزینهٔ retry و trialهای شکست‌خورده در گزارش حساب شود.

هیچ فرمان موجود در quick start تماس API، download وزن یا اجارهٔ GPU ندارد. latency smoke زمان یک baseline ساختگی است و نباید در مقاله با latency مدل واقعی مقایسه شود.

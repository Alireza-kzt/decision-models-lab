# 05 — مهندسی حافظه و اجرای مدل

[راهنما](README.md). این خانواده عمدتاً اهرم مهندسی است؛ کاربرد یک kernel موجود به‌تنهایی ادعای نوآوری الگوریتمی نیست. پیشنهادها هنوز اجرا نشده‌اند.

## T042 — FlashAttention

**اصل و منبع:** attention با بهینه‌سازی انتقال حافظه و محاسبهٔ tiled؛ [FlashAttention](https://arxiv.org/abs/2205.14135).

**انتقال و آزمون:** برای state و schema بلند، attention استاندارد و kernel سازگار را با precision، mask و batch یکسان مقایسه کنیم. خروجی‌ها باید در tolerance عددی توافق داشته باشند.

**پیش‌نیاز و ریسک:** W/F و پشتیبانی kernel؛ mask سفارشی decision model ممکن است پشتیبانی نشود. **FlashAttention با DFlash متفاوت است.**

## T043 — Grouped-query attention / GQA

**اصل و منبع:** اشتراک key/value میان گروه‌هایی از query headها؛ [GQA](https://arxiv.org/abs/2305.13245).

**انتقال و آزمون:** backbone سازگار با GQA در برابر MHA؛ اثر کیفیت، حافظه و context بلند را بسنجیم، نه فقط حافظهٔ KV-cache.

**پیش‌نیاز و ریسک:** W؛ تغییر ساختاری معمولاً نیازمند سازگارسازی است. در classifier تک‌مرحله‌ای بدون decoding، سود KV-cache ممکن است کوچک باشد.

## T044 — PagedAttention / vLLM

**اصل و منبع:** مدیریت صفحه‌ای حافظهٔ attention برای serving؛ [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180).

**انتقال و آزمون:** baseline مولد با درخواست‌های هم‌زمان و طول‌های متغیر؛ throughput و p95 در الگوی ترافیک ثابت اندازه‌گیری شوند.

**پیش‌نیاز و ریسک:** A و serving سازگار؛ یک decision head سفارشی الزاماً قابل اجرا در این engine نیست. batching نباید عدالت مقایسه را مخدوش کند.

## T045 — ZeRO

**اصل و منبع:** توزیع وضعیت‌های آموزش میان دستگاه‌ها؛ [ZeRO](https://arxiv.org/abs/1910.02054).

**انتقال و آزمون:** برای full FT بزرگ، peak memory، throughput و هزینهٔ ارتباط stageهای قابل استفاده مقایسه شوند.

**پیش‌نیاز و ریسک:** W و سخت‌افزار توزیع‌شده؛ این روش جایگزین LoRA یا quantization نیست و ارتباط می‌تواند گلوگاه شود. هیچ اجرای چندGPU در این بانک انجام نشده است.

## T046 — Activation checkpointing

**اصل و منبع:** ذخیرهٔ activation کمتر و بازحساب در backward؛ [Training Deep Nets with Sublinear Memory Cost](https://arxiv.org/abs/1604.06174).

**انتقال و آزمون:** تحت batch و sequence length ثابت، کاهش peak VRAM و افزایش زمان هر گام گزارش شود؛ یک سناریوی batch بزرگ‌تر جدا سنجیده شود.

**پیش‌نیاز و ریسک:** W؛ ابزار کاهش حافظهٔ آموزش است، نه شتاب inference. randomness و dropout در بازحساب باید درست مدیریت شوند.

## T047 — Mixed-precision training

**اصل و منبع:** استفادهٔ ترکیبی از دقت‌های عددی در آموزش؛ [Mixed Precision Training](https://arxiv.org/abs/1710.03740).

**انتقال و آزمون:** precisionهای پشتیبانی‌شده با مسیر مرجع مقایسه شوند؛ NaN/overflow، loss، احتمال‌های نهایی و حافظه ثبت شوند.

**پیش‌نیاز و ریسک:** W و سخت‌افزار سازگار؛ reductions حساس و normalization احتمالات ممکن است دقت بالاتر بخواهند. نوع داده و scaler را در manifest ثبت کنیم.

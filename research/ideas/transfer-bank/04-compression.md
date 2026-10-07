# 04 — فشرده‌سازی، تقطیر و ادغام

[راهنمای بانک](README.md). وضعیت همهٔ انتقال‌ها: **documented / untested-in-this-lab**. کیفیت احتمالات و سرعت واقعی باید مستقل از حجم فایل سنجیده شوند.

## T032 — Knowledge distillation

**اصل و منبع:** آموزش دانش‌آموز با توزیع نرم معلم؛ [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531).

**انتقال و آزمون:** distillation توزیع گزینه‌ها، همراه با برچسب درست؛ مقایسهٔ دانش‌آموز با CE تنها و با معلم. دما، وزن loss و انتقال به schema ندیده جدا بررسی شوند.

**پیش‌نیاز و ریسک:** W برای دانش‌آموز و P برای معلم؛ خطای معلم منتقل می‌شود. پاسخ top-1 جایگزین توزیع کامل نیست و گزینه‌های دو طرف باید هم‌معنا باشند.

## T033 — Intermediate-feature distillation / TinyBERT

**اصل و منبع:** انتقال بازنمایی‌ها و attentionهای میانی؛ [TinyBERT](https://arxiv.org/abs/1909.10351).

**انتقال و آزمون:** تقطیر ویژگی state و schema، علاوه بر logits؛ logit-only و feature+logit را در اندازهٔ دانش‌آموز ثابت مقایسه کنیم.

**پیش‌نیاز و ریسک:** F/W؛ نگاشت لایه‌ها و ابعاد لازم است. شباهت بازنمایی الزاماً بهترین معیار برای تصمیم نهایی نیست.

## T034 — Quantization-aware training

**اصل و منبع:** مدل‌کردن اثر کوانتیزه‌سازی هنگام آموزش؛ [Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference](https://arxiv.org/abs/1712.05877).

**انتقال و آزمون:** QAT برای decision head یا backbone؛ مقایسه با post-training quantization در همان bit-width. NLL، رتبه‌بندی گزینه‌های نزدیک و تأخیر سخت‌افزار مقصد ثبت شوند.

**پیش‌نیاز و ریسک:** W؛ fake quantization در آموزش تضمین kernel سریع در استنتاج نیست. هزینهٔ آموزش اضافه در گزارش بیاید.

## T035 — GPTQ

**اصل و منبع:** کوانتیزه‌سازی پس از آموزش با تقریب اطلاعات مرتبهٔ دوم؛ [GPTQ](https://arxiv.org/abs/2210.17323).

**انتقال و آزمون:** checkpoint تصمیم را با calibration corpus مستقل کوانتیزه کنیم؛ کیفیت، حافظه و سرعت با مدل اصلی مقایسه شوند.

**پیش‌نیاز و ریسک:** W و نمونهٔ ورودی؛ corpus کوانتیزه‌سازی از test جدا باشد. سازگاری لایه‌ها و kernel قبل از انتخاب بررسی شود.

## T036 — AWQ

**اصل و منبع:** کوانتیزه‌سازی وزن با توجه به activationها؛ [AWQ](https://arxiv.org/abs/2306.00978).

**انتقال و آزمون:** AWQ و GPTQ در precision و سخت‌افزار برابر؛ drift احتمال‌های تصمیم و افت گزینه‌های کم‌تکرار بررسی شود.

**پیش‌نیاز و ریسک:** W/F؛ نتایج مدل زبانی به head سفارشی خودکار منتقل نمی‌شوند. حفظ accuracy می‌تواند تغییر calibration را پنهان کند.

## T037 — SmoothQuant

**اصل و منبع:** انتقال بخشی از دشواری کوانتیزه‌سازی activation به وزن؛ [SmoothQuant](https://arxiv.org/abs/2211.10438).

**انتقال و آزمون:** کوانتیزه‌سازی وزن و activation یک encoder تصمیم؛ با weight-only تحت حافظه و latency واقعی مقایسه کنیم.

**پیش‌نیاز و ریسک:** W/F؛ outlierهای schemaهای جدید ممکن است با calibration corpus متفاوت باشند. operatorهای head باید جدا ارزیابی شوند.

## T038 — SparseGPT

**اصل و منبع:** هرس بزرگ‌مقیاس پس از آموزش؛ [SparseGPT](https://arxiv.org/abs/2301.00774).

**انتقال و آزمون:** هرس backbone با head ثابت، سپس بازآموزی اختیاری head به‌عنوان ablation مستقل؛ کیفیت و calibration قبل و بعد ثبت شوند.

**پیش‌نیاز و ریسک:** W/F؛ sparsity بدون kernel مناسب سرعت نمی‌آورد. هرس و fine-tuning را هم‌زمان تغییر ندهیم و اثرها را مخلوط نکنیم.

## T039 — Wanda

**اصل و منبع:** امتیاز هرس بر اساس اندازهٔ وزن و activation؛ [A Simple and Effective Pruning Approach for Large Language Models](https://arxiv.org/abs/2306.11695).

**انتقال و آزمون:** Wanda، magnitude pruning و SparseGPT با sparsity یکسان؛ پایداری روی ورودی‌های بلند و گزینه‌های نادر بررسی شود.

**پیش‌نیاز و ریسک:** W/F؛ metric هرس ممکن است با اهمیت واقعی برای تصمیم تخصصی هم‌راستا نباشد.

## T040 — Model soups

**اصل و منبع:** میانگین‌گیری وزن checkpointهای سازگار؛ [Model soups](https://arxiv.org/abs/2203.05482).

**انتقال و آزمون:** ادغام چند fine-tune از یک مبنا؛ با بهترین مدل منفرد و ensemble خروجی مقایسه شود. انتخاب اعضا فقط روی dev انجام شود.

**پیش‌نیاز و ریسک:** W؛ معماری، ترتیب پارامتر و معنای headها باید منطبق باشند. میانگین مدل‌های نامرتبط معتبر نیست.

## T041 — TIES merging

**اصل و منبع:** کاهش تداخل علامت و مؤلفه‌های کم‌اثر هنگام ادغام task vectorها؛ [TIES-Merging](https://arxiv.org/abs/2306.01708).

**انتقال و آزمون:** ادغام سازگارسازی‌های چند دامنه از مبنای یکسان؛ با میانگین ساده، انتخاب adapter و multi-task training مقایسه شود.

**پیش‌نیاز و ریسک:** W؛ ادغام چند مدل تخصصی به معنی حفظ عملکرد همهٔ گروه‌ها نیست. سازگاری head و tokenizer باید صریح ثبت شود.

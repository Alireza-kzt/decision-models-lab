# 07 — کالیبراسیون، عدم‌قطعیت و امتناع

[راهنما](README.md). همهٔ پیشنهادها **آزمایش‌نشده** هستند. احتمال عددی با احتمال کالیبره متفاوت است؛ تضمین آماری همیشه همراه با فرض و دامنهٔ اعتبار ثبت شود.

## T058 — Temperature scaling

**اصل و منبع:** بازتنظیم دمای logits روی مجموعهٔ calibration مستقل؛ [On Calibration of Modern Neural Networks](https://arxiv.org/abs/1706.04599).

**انتقال و آزمون:** global temperature در برابر دمای وابسته به نوع تصمیم؛ NLL، Brier و reliability bins در تعداد گزینه‌ها و دامنه‌های متفاوت سنجیده شوند.

**پیش‌نیاز و ریسک:** P؛ نمونهٔ calibration باید جدا باشد. دمای مثبت مشترک argmax را تغییر نمی‌دهد؛ انتظار افزایش accuracy از آن نداشته باشیم.

## T059 — Deep ensembles

**اصل و منبع:** تجمیع خروجی چند مدل آموزش‌دیده؛ [Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles](https://arxiv.org/abs/1612.01474).

**انتقال و آزمون:** چند seed یا adapter مستقل؛ با تک‌مدل هم‌هزینه و میانگین وزن مقایسه شود. disagreement و رفتار OOD ثبت شوند.

**پیش‌نیاز و ریسک:** W/P؛ خطاهای هم‌بسته و چندبرابرشدن هزینه. ensemble تضمین مصونیت از خطای مطمئن ندارد.

## T060 — MC dropout

**اصل و منبع:** نمونه‌گیری با dropout برای تقریب عدم‌قطعیت؛ [Dropout as a Bayesian Approximation](https://arxiv.org/abs/1506.02142).

**انتقال و آزمون:** چند forward با dropout در head یا backbone؛ در برابر ensemble و entropy تک‌مدل، risk/coverage و latency سنجیده شوند.

**پیش‌نیاز و ریسک:** W/F؛ فعال‌کردن کل train mode می‌تواند رفتار لایه‌های دیگر را ناخواسته تغییر دهد. تعداد نمونه‌ها در هزینه محاسبه شود.

## T061 — Adaptive conformal prediction sets

**اصل و منبع:** ساخت مجموعهٔ پاسخ با پوشش آماری؛ [Classification with Valid and Adaptive Coverage](https://arxiv.org/abs/2006.02544).

**انتقال و آزمون:** بازگرداندن مجموعهٔ گزینه‌ها به‌جای یک پاسخ؛ اندازهٔ مجموعه و پوشش روی test مستقل گزارش شوند. تغییر تعداد گزینه و دامنه stress test جدا باشد.

**پیش‌نیاز و ریسک:** P و calibration؛ پوشش معمولاً marginal و تحت exchangeability است، نه تضمین هر نمونه یا هر زیرگروه. OOD دلخواه تحت این تضمین نیست.

## T062 — Selective prediction / SelectiveNet

**اصل و منبع:** یادگیری پیش‌بینی همراه با گزینهٔ رد؛ [SelectiveNet](https://arxiv.org/abs/1901.09192).

**انتقال و آزمون:** abstention head برای تصمیم نامطمئن؛ با threshold entropy و conformal sets در coverage یکسان مقایسه شود.

**پیش‌نیاز و ریسک:** W و تعریف هزینهٔ رد؛ ردکردن همهٔ موارد دشوار می‌تواند گروه خاصی را محروم کند. پوشش گروهی و خطای پذیرفته‌شده‌ها هم گزارش شوند.

## T063 — Focal loss

**اصل و منبع:** کاهش وزن نمونه‌های آسان در loss؛ [Focal Loss for Dense Object Detection](https://arxiv.org/abs/1708.02002).

**انتقال و آزمون:** تصمیم‌های نامتوازن یا کم‌نمونه؛ با CE، class weighting و sampling برابر مقایسه شود. recall کلاس نادر و calibration جدا سنجیده شوند.

**پیش‌نیاز و ریسک:** W؛ تمرکز بر موارد سخت ممکن است label noise را تقویت کند. بهبود F1 تضمین بهبود NLL نیست.

## T064 — Label smoothing

**اصل و منبع:** نرم‌کردن targetهای آموزشی؛ [Rethinking the Inception Architecture for Computer Vision](https://arxiv.org/abs/1512.00567).

**انتقال و آزمون:** smoothing ثابت در برابر targetهای معلم و CE؛ مقیاس آن روی dev انتخاب شود و اثرش با تغییر تعداد گزینه‌ها بررسی شود.

**پیش‌نیاز و ریسک:** W؛ توزیع جرم روی گزینه‌های نامعتبر می‌تواند با قرارداد مسئله تعارض داشته باشد. smoothing به‌تنهایی برچسب اشتباه را اصلاح نمی‌کند.

## T065 — Bayesian LoRA / Laplace-LoRA

**اصل و منبع:** عدم‌قطعیت بیزی برای سازگارسازی کم‌رتبه؛ [Bayesian Low-rank Adaptation for Large Language Models](https://arxiv.org/abs/2308.13111).

**انتقال و آزمون:** posterior تقریبی برای LoRA یا head تصمیم؛ با LoRA نقطه‌ای، temperature scaling و ensemble در budget مشخص مقایسه شود.

**پیش‌نیاز و ریسک:** W/F؛ تقریب posterior و هزینهٔ curvature. «LoRA + عدم‌قطعیت» خودِ ایدهٔ تازه نیست؛ مسئله و تفاوت پیشنهادی باید دقیق‌تر شوند.

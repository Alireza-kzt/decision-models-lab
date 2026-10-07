# ۱۲ طرح ترکیبی برای ایده‌پردازی

[بانک روش‌ها](README.md) · [پروتکل](EVALUATION.md). وضعیت C001–C012: **proposed / not-run / novelty-unverified**. اجزا روش‌های موجودند؛ ترکیب آن‌ها به‌خودی‌خود ادعای مقاله نیست. معیارهای پذیرش و حد عملی اثر پیش از test تعیین شوند.

## C001 — LoRA × ساختار مجموعه‌ای گزینه‌ها

روش‌ها: T006 و T049/T050؛ مرتبط با [H001](../H001-schema-equivariance.md).

**سؤال:** آیا head هم‌وردا نسبت به جایگشت، حساسیت LoRA به ترتیب و اندازهٔ مجموعهٔ گزینه را کم می‌کند؟ طراحی ۲×۲: head معمولی/مجموعه‌ای و head-only/LoRA. کنترل تعداد پارامتر و split بر اساس schema. **ابطال:** کاهش حساسیت با افت کیفیت بیشتر از حد ازپیش‌تعریف‌شده، یا نبود سود نسبت به augmentation سادهٔ ترتیب.

## C002 — QLoRA × کالیبراسیون تحت تغییر schema

روش‌ها: T007 و T058؛ مرتبط با [H002](../H002-candidate-set-calibration.md).

**سؤال:** آیا quantization ساختار خطای confidence را در تعداد گزینهٔ جدید عوض می‌کند؟ LoRA دقیق‌تر/QLoRA، هرکدام با و بدون temperature scaling. **ابطال:** تفاوت با خطای نمونه‌گیری توضیح داده شود یا scaling عمومی به‌اندازهٔ روش تخصصی خوب باشد. accuracy، NLL، Brier و latency کنار هم گزارش شوند.

## C003 — LoRAMoE × تعمیم router به schema ندیده

روش‌ها: T021، T019 و T005؛ مرتبط با H001/H007.

**سؤال:** router وابسته به state/schema روی خانوادهٔ ندیده چه زمانی از adapter منفرد بهتر است؟ کنترل‌ها: single LoRA هم‌بودجه، routing دستی نوع وظیفه، router آموخته‌شده؛ shared expert یک ablation جدا. **ابطال:** سود فقط از افزایش ظرفیت یا دانستن نام دامنه ناشی شود. [LoRAMoE پیشینهٔ مستقیم است](https://arxiv.org/abs/2312.09979).

## C004 — Active learning × Distillation

روش‌ها: T069 و T032؛ مرتبط با [H006](../H006-few-label-transfer.md).

**سؤال:** کدام ترکیب query انسانی و توزیع معلم بیشترین سود در بودجهٔ برچسب ثابت دارد؟ random/active selection با hard labels/soft teacher در طراحی ۲×۲. **ابطال:** انتخاب uncertainty فقط نمونه‌های پرنویز را جذب کند یا در هزینهٔ واقعی انسان از random بهتر نباشد.

## C005 — Retrieval × امتناع شواهدمحور

روش‌ها: T081 و T062؛ مرتبط با [H003](../H003-evidence-aware-abstention.md).

**سؤال:** در نبود یا تناقض شواهد، مدل به‌جای پاسخ مطمئن غلط امتناع می‌کند؟ no/real/shuffled retrieval با entropy threshold/learned reject مقایسه شود. **ابطال:** سود به corpus دارای پاسخ test وابسته باشد یا پوشش گروه‌های مهم بدون کاهش ریسک کافی فروبریزد.

## C006 — Early exit × کنترل ریسک

روش‌ها: T030، T058 و T061؛ مرتبط با [H005](../H005-risk-controlled-cascade.md).

**سؤال:** در چه پوششی خروج زودهنگام به تأخیر کمتر با ریسک قابل کنترل می‌رسد؟ full depth، entropy exit و روش کالیبره را مقایسه کنیم. **ابطال:** هزینهٔ headهای میانی سود را از بین ببرد. تضمین conformal فقط در صورت برقرار بودن فرض‌ها و برای قرارداد ازپیش‌تعریف‌شده بیان شود، نه برای OOD دلخواه.

## C007 — چندفیلدی diffusion × قیود

روش‌ها: T101/T102 و T092/T093؛ مرتبط با [H004](../H004-structured-consistency.md).

**سؤال:** آیا refinement موازی برای تصمیم‌های وابسته از independent heads+repair بهتر است؟ AR head، joint head، diffusion بدون قید و diffusion با قید؛ اندازهٔ model و بودجهٔ inference جدا کنترل شوند. **ابطال:** قید فقط syntactic validity را بهتر کند ولی خطای معنایی یا زمان بیشتر شود.

## C008 — Policy–Value × نظارت مرحله‌ای

روش‌ها: T095 و T077؛ مرتبط با [H008](../H008-policy-value-search.md).

**سؤال:** آیا PRM با دادهٔ مرحله‌ای برابر تعداد nodeهای لازم برای رسیدن به پاسخ معتبر را کم می‌کند؟ search بدون یادگیری، policy-only، policy+outcome-value و policy+process-value. **ابطال:** oracle leakage، برتری ناشی از query بیشتر، یا نبود سود در مسئله‌های ندیده. تعداد مسئلهٔ حل‌شده و feasibility با oracle مستقل سنجیده شوند.

## C009 — Quantization/pruning × پایداری رتبه و confidence

روش‌ها: T035/T036/T038 و T058؛ مرتبط با H002/H003.

**سؤال:** چه تغییری در گزینه‌های تقریباً هم‌امتیاز رخ می‌دهد که accuracy میانگین پنهان می‌کند؟ quantization و pruning جدا اجرا شوند؛ هرکدام با و بدون recalibration. **ابطال:** metric پیشنهادی اطلاعاتی فراتر از NLL و margin baseline ندهد. سرعت باید روی kernel واقعاً sparse/quantized اندازه‌گیری شود.

## C010 — Hypernetwork × انتقال چندنمونه‌ای schema

روش‌ها: T054 و T098؛ مرتبط با H001/H006.

**سؤال:** head تولیدشده از توضیح schema به اندازهٔ adapter جدا داده نیاز دارد؟ hypernetwork، embedding-label scorer و LoRA با برچسب برابر؛ meta-learning یک مرحلهٔ جدا پس از baseline است. **ابطال:** مزیت فقط حفظ template باشد و با split خانواده‌ای ناپدید شود.

## C011 — Contrastive learning × تصمیم دوزبانه

روش‌ها: T052/T053 و T005؛ مرتبط با [H007](../H007-cross-lingual-decisions.md).

**سؤال:** آیا هم‌ترازی state و گزینه، اختلاف تصمیم فارسی/انگلیسی را در نمونه‌های هم‌معنا کم می‌کند؟ CE-only، contrastive+CE و ترجمه در inference. **ابطال:** ترجمهٔ نامعتبر، تفاوت معنایی گزینه‌ها یا نشت جفت ترجمه بین train/test. هر جفت و paraphraseهایش یک گروه split باشند.

## C012 — DFlash برای baseline مولدِ تصمیم ساخت‌یافته

روش‌ها: T028 و T027/T107؛ مرتبط با H004/H005، ولی فقط برای معماری مولد مناسب.

**سؤال:** برای چند فیلد و خروجی‌های بلند، drafter چه زمانی از decoding عادی سریع‌تر است؟ AR معمولی، EAGLE-3، DFlash و single-pass decision head؛ هزینهٔ آماده‌سازی مدل جدا گزارش شود. **ابطال:** طول خروجی کم یا سربار verify سود را از بین ببرد. ترکیب با grammar نیازمند بررسی الگوریتم پذیرش و توزیع است؛ تضمین خودکار ندارد.

## تبدیل طرح به پروژه

برای هر C ابتدا یک experiment record مستقل بسازید: مسئله، نوع دسترسی، منابع دقیق، نزدیک‌ترین کار مشابه، فرضیهٔ قابل رد، primary metric، اثر حداقلی مهم، budget، seedها، split و baseline. وضعیت proposed فقط با run artifact واقعی تغییر می‌کند. نتیجهٔ منفی و هزینهٔ شکست نیز در همین بانک باقی بمانند.

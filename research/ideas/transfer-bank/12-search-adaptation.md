# 12 — جست‌وجو، یادگیری از تعامل و سازگاری مداوم

[راهنما](README.md). طرح‌های زیر هنوز اجرا نشده‌اند. نتیجهٔ solver، simulator یا کارشناس باید با provenance مشخص ذخیره شود.

## T095 — Policy–Value + MCTS

**اصل و منبع:** policy و value آموخته‌شده برای هدایت جست‌وجو؛ [Mastering Chess and Shogi by Self-Play](https://arxiv.org/abs/1712.01815).

**انتقال و آزمون:** policy روی اقدام‌های مجاز و value روی stateهای جزئی؛ policy-only، search-only و policy+value با تعداد node یا زمان برابر مقایسه شوند.

**پیش‌نیاز و ریسک:** W/R؛ transition، reward، termination و action mask باید دقیق تعریف شوند. value بالای مدل یا خودِ MCTS تضمین بهینگی سراسری نیست.

## T096 — DAgger

**اصل و منبع:** جمع‌آوری supervision در stateهایی که policy خودش می‌بیند؛ [A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning](https://arxiv.org/abs/1011.0686).

**انتقال و آزمون:** اصلاح تصمیم‌های policy توسط oracle در trajectoryهای واقعی؛ با behavioral cloning و دادهٔ تصادفی در تعداد query برابر مقایسه شود.

**پیش‌نیاز و ریسک:** W/R و oracle؛ query به انسان یا solver می‌تواند گران باشد. stateهای test وارد فرایند آموزش نشوند.

## T097 — Elastic Weight Consolidation

**اصل و منبع:** محدودکردن تغییر پارامترهای مهم برای وظایف قبلی؛ [Overcoming catastrophic forgetting in neural networks](https://arxiv.org/abs/1612.00796).

**انتقال و آزمون:** افزودن دامنه یا schema تازه با retention روی نسخه‌های قبلی؛ با replay، adapter مستقل و fine-tuning عادی مقایسه شود.

**پیش‌نیاز و ریسک:** W و تخمین اهمیت؛ پایداری و پلاستیسیته trade-off دارند. افت عملکرد قبلی باید حتی با رشد میانگین کلی گزارش شود.

## T098 — MAML / Meta-learning

**اصل و منبع:** یادگیری initialization مناسب سازگاری سریع؛ [Model-Agnostic Meta-Learning](https://arxiv.org/abs/1703.03400).

**انتقال و آزمون:** هر schema یا دامنه یک task؛ در چند بودجهٔ برچسب به taskهای کاملاً ندیده سازگار شویم. با multi-task pretraining+LoRA و head-only مقایسه شود.

**پیش‌نیاز و ریسک:** W؛ meta-train و meta-test باید از نظر خانوادهٔ مسئله جدا باشند. چند برابرشدن هزینهٔ inner/outer loop لحاظ شود.

## T099 — Group DRO

**اصل و منبع:** بهینه‌سازی مقاومت در برابر گروه‌های مسئله؛ [Distributionally Robust Neural Networks for Group Shifts](https://arxiv.org/abs/1911.08731).

**انتقال و آزمون:** گروه‌بندی زبان، پیچیدگی schema یا منبع داده؛ worst-group و average عملکرد با ERM و reweighting ساده مقایسه شوند.

**پیش‌نیاز و ریسک:** W و group labels قابل اعتماد؛ عملکرد گروه‌های ناشناخته تضمین نمی‌شود. گروه‌بندی پس از دیدن نتیجهٔ test سوگیری ایجاد می‌کند.

## T100 — Test-time adaptation / Tent

**اصل و منبع:** سازگارسازی زمان آزمون با هدف entropy؛ [Tent](https://arxiv.org/abs/2006.10726).

**انتقال و آزمون:** سناریوی stream جدید بدون برچسب، با قرارداد adaptation از پیش تعیین‌شده؛ با frozen model و calibration ثابت مقایسه شود. reset و ترتیب ورود نمونه‌ها ثبت شوند.

**پیش‌نیاز و ریسک:** W؛ کم‌شدن entropy ممکن است افزایش اطمینانِ اشتباه باشد. نتایج transductive یا online را با ارزیابی frozen یکسان گزارش نکنیم.

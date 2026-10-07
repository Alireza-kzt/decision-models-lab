# 09 — هدف آموزشی، ترجیح و یادگیری تقویتی

[راهنما](README.md). استفادهٔ نام یک الگوریتم RL روی یک classifier، به‌تنهایی صورت‌بندی صحیح ایجاد نمی‌کند. action، reward، policy و baseline باید پیش از اجرا تعریف شوند. تمام آزمون‌ها پیشنهادی‌اند.

## T073 — PPO

**اصل و منبع:** بهینه‌سازی policy با objective محدودشده؛ [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347).

**انتقال و آزمون:** وقتی تصمیم بر پاداش محیط اثر دارد، policy گزینه‌ها را با PPO تنظیم کنیم؛ با CE روی پاسخ‌های oracle و contextual-bandit ساده مقایسه شود.

**پیش‌نیاز و ریسک:** W/R؛ reward hacking و ناپایداری. برای classification برچسب‌دار مستقل، RL لزوماً لازم یا بهتر نیست.

## T074 — RLHF

**اصل و منبع:** آموزش با ترجیح انسانی و reward model؛ [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155).

**انتقال و آزمون:** ترجیح انسان میان تصمیم‌های چندمعیاره؛ reward model و policy را جدا ارزیابی کنیم. supervised preference classifier و انتخاب با امتیاز ثابت baseline باشند.

**پیش‌نیاز و ریسک:** W/R و annotation ترجیحی؛ توافق داوران، سوگیری reward و جدایی افراد/مسائل در split. ترجیح ذهنی معادل صحت عینی نیست.

## T075 — DPO

**اصل و منبع:** بهینه‌سازی مستقیم از جفت پاسخ ترجیحی؛ [Direct Preference Optimization](https://arxiv.org/abs/2305.18290).

**انتقال و آزمون:** جفت تصمیم بهتر/بدتر در یک state و reference policy مشخص؛ با pairwise ranking و CE مقایسه شود. سازگاری تعریف احتمال در head تصمیم بررسی شود.

**پیش‌نیاز و ریسک:** W و دادهٔ ترجیح؛ تغییر از احتمال توالی به action distribution باید صریح صورت‌بندی شود. افزایش ترجیح می‌تواند calibration را بدتر کند.

## T076 — GRPO

**اصل و منبع:** policy optimization با مقایسهٔ پاداش اعضای یک گروه؛ [DeepSeekMath](https://arxiv.org/abs/2402.03300).

**انتقال و آزمون:** چند تصمیم یا مسیر برای یک مسئله با reward قابل محاسبه؛ در برابر PPO و best-of-N با بودجهٔ نمونه‌گیری برابر مقایسه شود.

**پیش‌نیاز و ریسک:** W/R؛ گروه با پاداش یکسان سیگنال کمی دارد. اعتبار schema به‌تنهایی reward کافی برای صحت معنایی نیست.

## T077 — Process supervision / PRM

**اصل و منبع:** نظارت بر مراحل میانی حل؛ [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050).

**انتقال و آزمون:** امتیاز مرحله‌ای برای زنجیرهٔ تصمیم‌ها یا جست‌وجو؛ outcome-only و process+outcome مقایسه شوند. ارزش PRM خارج از نمونه‌های آموزش بررسی شود.

**پیش‌نیاز و ریسک:** R و برچسب معتبر مراحل؛ rationale تولیدشده خودبه‌خود trace واقعی تصمیم نیست. هزینهٔ برچسب‌های مرحله‌ای در مقایسه لحاظ شود.

## T078 — PCGrad

**اصل و منبع:** کاهش تضاد gradientهای وظایف؛ [Gradient Surgery for Multi-Task Learning](https://arxiv.org/abs/2001.06782).

**انتقال و آزمون:** برای Choice، Score و abstention، lossهای جدا با PCGrad؛ با مجموع ساده و وزن‌دهی ثابت در همان backbone مقایسه شود.

**پیش‌نیاز و ریسک:** W؛ هزینهٔ چند gradient و حساسیت به batch. کاهش تضاد gradient الزاماً بهبود همهٔ وظایف نیست.

## T079 — Uncertainty-based task weighting

**اصل و منبع:** وزن‌دهی چند loss با پارامترهای uncertainty وظیفه؛ [Multi-Task Learning Using Uncertainty to Weigh Losses](https://arxiv.org/abs/1705.07115).

**انتقال و آزمون:** تنظیم مشترک طبقه‌بندی، score و value؛ با normalization و وزن‌های grid-searched مقایسه شود.

**پیش‌نیاز و ریسک:** W؛ uncertainty این loss با predictive uncertainty کالیبره یکسان نیست. مقیاس targetهای متفاوت باید ثبت شود.

## T080 — Ordinal regression / CORAL

**اصل و منبع:** یادگیری رتبه‌های ترتیبی با سازگاری آستانه‌ها؛ [Rank Consistent Ordinal Regression for Neural Networks](https://arxiv.org/abs/1901.07884).

**انتقال و آزمون:** خروجی Score با رتبه‌های مرتب؛ با nominal CE و regression عادی مقایسه شود. خطای فاصلهٔ رتبه و calibration آستانه‌ها گزارش شوند.

**پیش‌نیاز و ریسک:** W؛ فقط برای برچسب واقعاً ترتیبی. مرتب‌سازی دلخواه نام گزینه‌ها مسئلهٔ ordinal ایجاد نمی‌کند.

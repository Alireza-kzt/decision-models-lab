# 13 — تولید موازی، diffusion و تصمیم گسسته

[راهنما](README.md). این خانواده راه‌های تولید یا انتخاب خروجی ساخت‌یافته را بررسی می‌کند. diffusion، classifier تک‌مرحله‌ای و speculative decoding سه مفهوم متفاوت‌اند. تمام انتقال‌های پیشنهادی هنوز اجرا نشده‌اند.

## T101 — Discrete diffusion / D3PM

**اصل و منبع:** فرایند diffusion در فضای گسسته؛ [Structured Denoising Diffusion Models in Discrete State-Spaces](https://arxiv.org/abs/2107.03006).

**انتقال و آزمون:** denoising بردار تصمیم‌های چندفیلدی شرطی بر state/schema؛ با independent heads و مدل autoregressive هم‌بودجه مقایسه شود.

**پیش‌نیاز و ریسک:** W؛ تعداد گام‌ها و توزیع corruption اهمیت دارند. ورودیِ inference نباید برچسب پاک target را دریافت کند. diffusion الزاماً یک‌مرحله‌ای یا سریع‌تر نیست.

## T102 — MaskGIT / Iterative parallel refinement

**اصل و منبع:** تولید و اصلاح موازی توکن‌های masked؛ [MaskGIT](https://arxiv.org/abs/2202.04200).

**انتقال و آزمون:** پرکردن و بازنگری فیلدهای تصمیم با confidence؛ یک pass، چند pass و انتخاب فیلد تصادفی مقایسه شوند. سازگاری مشترک و wall time سنجیده شوند.

**پیش‌نیاز و ریسک:** W؛ confidence نامعتبر می‌تواند پاسخ غلط را زود قفل کند. منبع اصلی تولید تصویر است؛ انتقال به typed decisions فرضیهٔ جداست.

## T103 — LLaDA / Masked diffusion language models

**اصل و منبع:** مدل زبانی مبتنی بر masked diffusion؛ [Large Language Diffusion Models](https://arxiv.org/abs/2502.09992).

**انتقال و آزمون:** baseline تولید schema با مدل diffusion در برابر AR و decision head؛ هزینهٔ کل forwardها، خطای معنایی و خروجی نامعتبر مقایسه شوند.

**پیش‌نیاز و ریسک:** W یا engine سازگار؛ likelihood و sampling با مدل AR یکسان نیستند. صرف non-autoregressive بودن، probability کالیبره یا تأخیر کمتر را تضمین نمی‌کند.

## T104 — Pointer Networks

**اصل و منبع:** اشاره به اعضای ورودی به‌جای vocabulary ثابت؛ [Pointer Networks، NeurIPS](https://papers.nips.cc/paper_files/paper/2015/hash/29921001f2f04bd3baee84a12e98098f-Abstract.html)، [arXiv](https://arxiv.org/abs/1506.03134).

**انتقال و آزمون:** انتخاب از مجموعهٔ گزینه‌های متغیر با pointer head؛ با fixed classifier و similarity scorer مقایسه شود. permutation و اندازهٔ مجموعهٔ ندیده تست شوند.

**پیش‌نیاز و ریسک:** W/F؛ اشارهٔ معتبر از نظر index، درستی معنایی انتخاب را ثابت نمی‌کند. نمایش ترتیبی می‌تواند سوگیری جایگاه بیاورد.

## T105 — Gumbel-Softmax

**اصل و منبع:** تقریب مشتق‌پذیر انتخاب دسته‌ای؛ [Categorical Reparameterization with Gumbel-Softmax](https://arxiv.org/abs/1611.01144).

**انتقال و آزمون:** آموزش router یا action selection در pipeline مشتق‌پذیر؛ با soft routing و estimatorهای مناسب دیگر در بودجهٔ برابر مقایسه شود.

**پیش‌نیاز و ریسک:** W؛ پاسخ نرم آموزش با اقدام سخت inference فرق دارد. temperature و estimator bias باید ثبت شوند، نه نادیده گرفته شوند.

## T106 — Gumbel-Sinkhorn

**اصل و منبع:** relaxation تصادفی برای permutation؛ [Learning Latent Permutations with Gumbel-Sinkhorn Networks](https://arxiv.org/abs/1802.08665).

**انتقال و آزمون:** تخصیص یک‌به‌یک چند گزینه یا منبع؛ با matching solver و انتخاب مستقل همراه repair مقایسه شود.

**پیش‌نیاز و ریسک:** W/R؛ relaxation doubly-stochastic و rounding می‌توانند خروجی متفاوت بدهند. همهٔ قیود دامنه در شرط تخصیص یک‌به‌یک خلاصه نمی‌شوند.

## T107 — PICARD / Constrained decoding

**اصل و منبع:** محدودکردن decoding با parsing افزایشی؛ [PICARD](https://arxiv.org/abs/2109.05093).

**انتقال و آزمون:** baseline مولد با grammar یا schema validator؛ unconstrained، constrained و decision head مقایسه شوند. نرخ خطای نحوی و معنایی جدا گزارش شوند.

**پیش‌نیاز و ریسک:** A/R؛ خروجی JSON صحیح یا query قابل parse می‌تواند پاسخ غلط داشته باشد. constraint checker جای verifier توزیعی speculative sampling نیست.

## T108 — STaR / Self-taught reasoning

**اصل و منبع:** تولید، انتخاب و استفادهٔ مجدد از rationales برای آموزش؛ [STaR](https://arxiv.org/abs/2203.14465).

**انتقال و آزمون:** معلم مولد مسیرهای حل می‌سازد، سپس دانش‌آموز تصمیم با supervision پالایش‌شده آموزش می‌بیند؛ با برچسب بدون rationale و distillation مستقیم مقایسه شود.

**پیش‌نیاز و ریسک:** W و معیار صحت مستقل؛ رسیدن به پاسخ درست، صحت rationale را تضمین نمی‌کند. انتخاب فقط نمونه‌های آسان می‌تواند داده را منحرف کند.

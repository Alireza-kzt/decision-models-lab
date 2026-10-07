# 06 — بازنمایی، ساختار گزینه‌ها و backbone

[راهنما](README.md). اصل روش‌ها از مقاله‌های لینک‌شده است؛ انتقال آن‌ها به تصمیم‌های typed و schemaهای متغیر پیشنهاد آزمایشگاه و **آزمایش‌نشده** است.

## T048 — Bidirectional decision encoder

**اصل و منبع:** استفاده از زمینهٔ دوطرفه در encoder؛ [BERT](https://arxiv.org/abs/1810.04805).

**انتقال و آزمون:** state، پرسش و گزینه‌ها با mask دوطرفه یا block mask پردازش شوند؛ causal، bidirectional و schema-aware mask با آموزش هم‌بودجه مقایسه شوند.

**پیش‌نیاز و ریسک:** W؛ حذف causal mask از checkpoint موجود بدون آموزش/ارزیابی، سازگاری را تضمین نمی‌کند. برچسب پاسخ نباید وارد attention شود.

## T049 — Deep Sets

**اصل و منبع:** بازنمایی مجموعه با ساختار ناوردا نسبت به جایگشت؛ [Deep Sets](https://arxiv.org/abs/1703.06114).

**انتقال و آزمون:** تجمیع متقارن گزینه‌ها و scorer مشترک برای هر گزینه؛ پس از permutation، احتمالات باید با همان permutation جابه‌جا شوند. تعداد گزینهٔ ندیده نیز آزمایش شود.

**پیش‌نیاز و ریسک:** W/F؛ خروجی کلی invariant و بردار امتیاز گزینه‌ها equivariant است. positional encoding یا ترتیب در serialization می‌تواند این خاصیت را بشکند.

## T050 — Set Transformer

**اصل و منبع:** attention برای مدل‌سازی تعامل اعضای مجموعه؛ [Set Transformer](https://arxiv.org/abs/1810.00825).

**انتقال و آزمون:** head مجموعه‌ای برای رقابت و وابستگی گزینه‌ها؛ با Deep Sets و independent scoring مقایسه شود. permutation و افزودن distractor کنترل شوند.

**پیش‌نیاز و ریسک:** W/F؛ افزایش ظرفیت و هزینهٔ attention را از سود ساختار مجموعه جدا کنیم. ترتیب ورودی نباید اطلاعات هدف را لو بدهد.

## T051 — Graph attention / GAT

**اصل و منبع:** تجمیع همسایگی با وزن‌های attention؛ [Graph Attention Networks](https://arxiv.org/abs/1710.10903).

**انتقال و آزمون:** گراف روابط بین فیلدها، گزینه‌ها یا اجزای مسئله؛ با head بدون گراف و گراف تصادفی مقایسه شود. خطای مشترک تصمیم‌ها و نقض قیود سنجیده شود.

**پیش‌نیاز و ریسک:** W/R؛ روابط باید در زمان inference در دسترس باشند. استفاده از پاسخ درست برای ساخت یال‌ها leakage است.

## T052 — Two-tower embeddings / Sentence-BERT

**اصل و منبع:** embedding قابل مقایسه برای متن‌ها؛ [Sentence-BERT](https://arxiv.org/abs/1908.10084).

**انتقال و آزمون:** encode مستقل state و توضیح گزینه، سپس similarity؛ با cross-encoder و head ثابت مقایسه شود. latency با cache گزینه‌ها و بدون آن گزارش شود.

**پیش‌نیاز و ریسک:** F/W؛ similarity الزاماً probability نیست. two-tower تعامل دقیق state و گزینه را محدود می‌کند.

## T053 — Contrastive representation learning / SimCSE

**اصل و منبع:** یادگیری embedding با جفت‌های مثبت و منفی؛ [SimCSE](https://arxiv.org/abs/2104.08821).

**انتقال و آزمون:** state و گزینهٔ درست مثبت، distractorهای معتبر منفی؛ با CE تنها و contrastive+CE مقایسه شود. تعمیم به نام‌گذاری جدید برچسب‌ها سنجیده شود.

**پیش‌نیاز و ریسک:** W؛ false negative و چند پاسخ صحیح. paraphrase معنایی با تغییر واقعی پاسخ مخلوط نشود.

## T054 — HyperNetworks

**اصل و منبع:** تولید پارامترهای شبکه توسط شبکه‌ای دیگر؛ [HyperNetworks](https://arxiv.org/abs/1609.09106).

**انتقال و آزمون:** head یا adapter شرطی بر توضیح schema؛ با head مشترک و adapter ثابت در schemaهای ندیده مقایسه شود.

**پیش‌نیاز و ریسک:** W؛ تولید وزن بزرگ گران و ناپایدار است. بهبود باید فراتر از استفادهٔ ساده از embedding توضیح برچسب باشد.

## T055 — Perceiver latent bottleneck

**اصل و منبع:** cross-attention از ورودی بزرگ به latentهای محدود؛ [Perceiver](https://arxiv.org/abs/2103.03206).

**انتقال و آزمون:** خلاصه‌سازی state بلند پیش از تصمیم‌های متعدد؛ با pooling ساده و attention کامل در چند اندازهٔ bottleneck مقایسه شود.

**پیش‌نیاز و ریسک:** W/F؛ جزئیات نادر و شواهد تعیین‌کننده ممکن است حذف شوند. accuracy کلی برای کشف این خطا کافی نیست.

## T056 — Mamba / Selective state-space models

**اصل و منبع:** مدل‌سازی توالی با state-space انتخابی؛ [Mamba](https://arxiv.org/abs/2312.00752).

**انتقال و آزمون:** یک encoder تصمیم با SSM و baseline attention در طول‌های مختلف؛ کیفیت بازیابی شواهد، حافظه و latency بررسی شوند.

**پیش‌نیاز و ریسک:** W؛ جایگزین مستقیم head یا mask نیست. معماری و kernel باید واقعاً پیاده‌سازی شوند و ترتیب گزینه‌ها کنترل شود.

## T057 — Sparse/global attention / Longformer

**اصل و منبع:** attention محلی همراه با مسیرهای global؛ [Longformer](https://arxiv.org/abs/2004.05150).

**انتقال و آزمون:** پرسش و schema global و state طولانی local؛ با full attention و truncation در بودجهٔ مشابه مقایسه شود.

**پیش‌نیاز و ریسک:** W؛ شواهد دور و ترکیبی ممکن است از دست بروند. انتخاب توکن‌های global از پاسخ هدف نباید استفاده کند.

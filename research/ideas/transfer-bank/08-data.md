# 08 — داده، انتخاب نمونه و supervision کم‌هزینه

[راهنما](README.md). وضعیت تمام انتقال‌ها: **documented / untested-in-this-lab**. دادهٔ مصنوعی جایگزین خودکار اعتبارسنجی انسانی و gold test مستقل نیست.

## T066 — Self-Instruct / Synthetic supervision

**اصل و منبع:** تولید وظایف و نمونه‌های آموزشی با مدل؛ [Self-Instruct](https://arxiv.org/abs/2212.10560).

**انتقال و آزمون:** تولید state/schema/گزینه با پاسخ قابل بررسی؛ مقایسهٔ gold-only، synthetic-only و mixed در بودجهٔ برچسب مشخص. یک نمونهٔ تصادفی توسط انسان یا oracle معتبر بازبینی شود.

**پیش‌نیاز و ریسک:** دسترسی مجاز به معلم و W برای دانش‌آموز؛ تکرار، آلودگی، سوگیری و خطای پاسخ مصنوعی. هزینه و شرایط استفاده از API جدا بررسی شوند.

## T067 — FixMatch / Pseudo-label consistency

**اصل و منبع:** ترکیب pseudo-label مطمئن و سازگاری در برابر augmentation؛ [FixMatch](https://arxiv.org/abs/2001.07685).

**انتقال و آزمون:** دو تبدیل واقعاً هم‌معنای state/schema؛ CE تنها، pseudo-label تنها و consistency را جدا مقایسه کنیم. سود در برچسب‌های کم سنجیده شود.

**پیش‌نیاز و ریسک:** W؛ augmentation تصویری مقاله مستقیماً برای متن تصمیم معتبر نیست. حذف نفی، تغییر عدد یا ترتیب شرط‌ها ممکن است پاسخ درست را عوض کند.

## T068 — DoReMi / Data-mixture optimization

**اصل و منبع:** بهینه‌سازی سهم دامنه‌های داده با مدل proxy؛ [DoReMi](https://arxiv.org/abs/2305.10429).

**انتقال و آزمون:** وزن‌دهی خانواده‌های تصمیم؛ مقایسه با uniform، proportional و weighting دستی، با تعداد کل نمونه و compute برابر.

**پیش‌نیاز و ریسک:** W و چند دامنهٔ مشخص؛ انتخاب mixture روی test ممنوع است. رفتار proxy کوچک ممکن است نمایندهٔ مدل نهایی نباشد.

## T069 — Bayesian active learning

**اصل و منبع:** انتخاب نمونه برای برچسب‌گذاری بر اساس عدم‌قطعیت؛ [Deep Bayesian Active Learning with Image Data](https://arxiv.org/abs/1703.02910).

**انتقال و آزمون:** انتخاب state/schemaهای مبهم برای human labeling؛ با انتخاب تصادفی، diversity و entropy در هزینهٔ برچسب برابر مقایسه شود.

**پیش‌نیاز و ریسک:** P یا مدل uncertainty، و oracle برچسب؛ ابهام ذاتی یا نویز ممکن است بودجه را مصرف کند. هر چرخه و زمان واقعی انسان ثبت شود.

## T070 — Hard-negative mining

**اصل و منبع:** آموزش با منفی‌های دشوار، نمونهٔ مرجع [Dense Passage Retrieval](https://arxiv.org/abs/2004.04906).

**انتقال و آزمون:** distractor نزدیک به پاسخ، به‌جای گزینه‌های تصادفی آسان؛ random negatives، mined negatives و ترکیب را با تعداد یکسان بسنجیم.

**پیش‌نیاز و ریسک:** W/F و تأیید برچسب؛ نزدیک‌ترین گزینه ممکن است واقعاً پاسخ معتبر دیگری باشد. mining نباید از test labels استفاده کند.

## T071 — mixup

**اصل و منبع:** ترکیب ورودی و target برای regularization؛ [mixup](https://arxiv.org/abs/1710.09412).

**انتقال و آزمون:** در embedding state و فقط میان نمونه‌های دارای فضای برچسب هم‌معنا؛ مقایسه با dropout و augmentation معنایی.

**پیش‌نیاز و ریسک:** W/F؛ مخلوط‌کردن دو schema با label indexهای متفاوت تعریف درستی ندارد. interpolation در متن یا فضای تصمیم همیشه معنای معتبر ندارد.

## T072 — Deduplication and contamination control

**اصل و منبع:** حذف تکرار از دادهٔ آموزش؛ [Deduplicating Training Data Makes Language Models Better](https://arxiv.org/abs/2107.06499).

**انتقال و آزمون:** گروه‌بندی template، paraphrase و منبع مشترک پیش از split؛ عملکرد random split و grouped split را به‌عنوان آزمون حساسیت جدا گزارش کنیم.

**پیش‌نیاز و ریسک:** دسترسی به corpus و provenance؛ dedup تقریب‌محور ممکن است مثبت کاذب داشته باشد. افت پس از حذف نشت نتیجهٔ ارزشمند است، نه دلیل بازگشت به split آلوده.

# فهرست مدل‌ها و مقاله‌ها

این فهرست، نقشهٔ مطالعه است نه leaderboard. تمام ورودی‌ها از صفحهٔ اصلی سازنده/نگه‌دارنده، صفحهٔ سرویس‌دهی یا arXiv بررسی شده‌اند. هیچ وزن دانلود و هیچ مدل این فهرست در آزمایشگاه اجرا نشده است.

منابع ماشین‌خوان اولیه: [مدل‌ها](../registry/models.json)، [مقاله‌ها](../registry/papers.json)، [منابع](../registry/sources.json). این سه فایل snapshot اولیهٔ ۷ اکتبر هستند. یافته‌های جدید در [supplement تاریخ‌دار ۸ اکتبر](../registry/updates/2026-10-08.json) ثبت شده‌اند؛ loader اجرایی هنوز آن را مصرف نمی‌کند.

## به‌روزرسانی ۸ اکتبر ۲۰۲۶

[گزارش یکپارچه](../research/updates/2026-10-08-jev-competitors.md) · [چهار آزمایش پیشنهادی](../research/experiments/2026-10-08-decision-model-screening.md)

- [Liquid d1-3B و d1-omni-600M](models/d1.md): کارت خانواده به‌روز شد؛ انتشار دو checkpoint با سرویس قبلی یکسان فرض نشده است.
- [SanSi](models/sansi.md): کارت مدل/مقالهٔ تصمیم حلقه‌ای؛ وضعیت کد و وزن جدا ثبت شده است.
- [Torchcast Decision 27B](models/torchcast-decision-27b.md): baseline مشروط با ملاحظات holdout و مجوز.
- [Labels Override Definitions](papers/labels-override-definitions.md): یادداشت مقاله و آزمون پیشنهادی نام گزینه در برابر تعریف.

## خانواده‌ها
خروجی غیرمولد، طبقه‌بند schema-conditioned، API تجاری، مدل حلقه‌ای و مدل مولد با پاسخ محدودشده باید جدا مقایسه شوند. «System One» در این مخزن دستهٔ کاربردی است؛ یک معماری یگانه و استاندارد فرض نمی‌شود.

## مدل‌های فهرست اولیه
- [Jev](models/jev.md) — `native_decision_service`
- [Clef / Clef-Flash](models/clef.md) — `native_decision_weights`
- [pplx-decider-v1.1-27b](models/pplx-decider.md) — `native_decision_weights`
- [GLiDE](models/glide.md) — `adaptive_decision_service`
- [GLiNER2.5-Decide](models/gliner-decide.md) — `schema_conditioned_encoder`
- [d1](models/d1.md) — سرویس تاریخی + کارت به‌روزشدهٔ دو checkpoint؛ نوع اولیه در runtime registry هنوز `native_decision_service` است.
- [Tev1-4B Experimental](models/tev1.md) — `constrained_generative_baseline`
- [Laya](models/laya.md) — `schema_conditioned_encoder`
- [Kev](models/kev.md) — `native_decision_weights`
- [Decider 1](models/decider1.md) — `native_decision_service`
- [Mercury Decide](models/mercury-decide.md) — `decision_endpoint`
- [StartLux-Decision](models/startlux.md) — `native_decision_weights`
- [Chinese-Jev](models/chinese-jev.md) — `schema_conditioned_encoder`
- [OpenAI Decisions API](models/openai-decisions.md) — `decision_api_product`

## مقاله‌های فهرست اولیه
- [P001 — GLiNER2: An Efficient Multi-Task Information Extraction System with Schema-Driven Interface](papers/P001.md)
- [P002 — Chinese-Jev: Bringing System One Model to Chinese-Language Tasks](papers/P002.md)
- [P003 — Benchmarking System One decision models against trained classifiers and language models for automated decision gates](papers/P003.md)
- [P004 — Evaluating and Benchmarking the System One Model Jev](papers/P004.md)
- [P005 — On Calibration of Modern Neural Networks](papers/P005.md)
- [P006 — A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification](papers/P006.md)
- [P007 — Deep Sets](papers/P007.md)

ورودی‌های تاریخی فوق در این به‌روزرسانی دوباره ممیزی نشده‌اند؛ جزئیات جدید فقط در supplement و کارت‌های مشخص‌شده آمده است.

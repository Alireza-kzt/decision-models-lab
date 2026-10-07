# بانک انتقال ایده از مدل‌های پیشین 🔬

تاریخ بررسی منابع: **2026-10-07**. نسخهٔ اولیه: **108 روش در 13 خانواده**. هدف، گردآوری مصالح پژوهش است؛ نه انتخاب موضوع نهایی و نه معرفی 108 نوآوری تازه. این فهرست گسترده و قابل توسعه است، نه ادعای پوشش همهٔ روش‌های تاریخ یادگیری ماشین.

[بازگشت به هشت فرضیهٔ آزمایشگاه](../README.md) · [چهار روش درخواستی](REQUESTED_METHODS.md) · [ترکیب‌ها و آزمایش‌های پیشنهادی](COMBINATIONS.md) · [پروتکل ارزیابی](EVALUATION.md) · [وضعیت شواهد](EVIDENCE.md)

## فهرست خانواده‌ها

| خانواده | شناسه‌ها | تعداد | نمونه‌ها |
|---|---|---:|---|
| [آموزش و سازگارسازی](01-adaptation.md) | T001–T015 | 15 | Full FT, LoRA, QLoRA, DoRA, AdaLoRA, Adapters, ReFT |
| [خبره‌ها و محاسبهٔ شرطی](02-experts.md) | T016–T023 | 8 | MoE, Switch, Expert Choice, Upcycling, LoRAMoE |
| [شتاب و پیش‌نویس‌سازی](03-acceleration.md) | T024–T031 | 8 | Speculative Decoding, Medusa, EAGLE, DFlash, DFlare, Early Exit |
| [فشرده‌سازی و ادغام مدل](04-compression.md) | T032–T041 | 10 | Distillation, GPTQ, AWQ, Pruning, Model Soups, TIES |
| [مهندسی حافظه و اجرا](05-systems.md) | T042–T047 | 6 | FlashAttention, GQA, PagedAttention, ZeRO, Checkpointing |
| [بازنمایی و backbone](06-representations.md) | T048–T057 | 10 | BERT, Deep Sets, Set Transformer, GNN, HyperNetworks, Mamba |
| [عدم‌قطعیت و قابلیت اتکا](07-reliability.md) | T058–T065 | 8 | Calibration, Ensembles, Conformal, Abstention, Laplace-LoRA |
| [داده و برچسب‌گذاری](08-data.md) | T066–T072 | 7 | Self-Instruct, FixMatch, DoReMi, Active Learning, Hard Negatives |
| [تابع هدف و یادگیری ترجیحی](09-objectives.md) | T073–T080 | 8 | PPO, RLHF, DPO, GRPO, Process Supervision, PCGrad |
| [بازیابی و استدلال](10-retrieval-reasoning.md) | T081–T088 | 8 | RAG, RETRO, kNN, ReAct, ToT, CoT, DSPy |
| [چندوجهی و قیود ساختاری](11-multimodal-constraints.md) | T089–T094 | 6 | CLIP, ViT, BLIP-2, DeepProbLog, OptNet, MAE |
| [جست‌وجو و سازگاری مداوم](12-search-adaptation.md) | T095–T100 | 6 | Policy–Value/MCTS, DAgger, EWC, MAML, Group DRO, Tent |
| [تولید موازی و تصمیم گسسته](13-discrete-generation.md) | T101–T108 | 8 | D3PM, MaskGIT, LLaDA, Pointer Networks, Gumbel, PICARD, STaR |

## هر مدخل چه می‌گوید؟

«اصل و منبع» خلاصهٔ یک روش موجود و لینک مقالهٔ اصلی یا نمونهٔ پژوهشی مرجع است. برای روش‌های عمومی مانند full fine-tuning، مقالهٔ لینک‌شده نمونهٔ کاربرد است، نه ادعای اولین اختراع روش. «انتقال و آزمون» پیشنهاد این آزمایشگاه است و هنوز اجرا نشده. «پیش‌نیاز و ریسک» مانع فنی، داده‌ای یا آماری را ثبت می‌کند. تمام مدخل‌های T001–T108 در وضعیت **documented / untested-in-this-lab** هستند.

### کدهای دسترسی

- **W**: دسترسی به وزن‌ها و امکان آموزش؛ **F**: دسترسی به ویژگی‌های داخلی یا embedding.
- **P**: احتمال یا logit همهٔ گزینه‌های مرتبط؛ API با فقط یک برچسب کافی نیست.
- **A**: کنترل فرایند decoding خودرگرسیو؛ **R**: محیط، ابزار، solver یا oracle قابل کنترل.

وجود یک API تجاری، W یا F را فراهم نمی‌کند. open-weight بودن نیز به‌تنهایی به معنی مجاز بودن استفادهٔ تجاری، بازتولید کامل آموزش یا پشتیبانی کتابخانهٔ ما نیست. قابلیت واقعی هر checkpoint باید در کارت مدل و revision آن بررسی شود.

### مرزهای ضروری

LoRA روش آموزش کم‌پارامتر است؛ MoE معماری محاسبهٔ شرطی؛ DFlash روش شتاب decoding. این‌ها هم‌سطح و قابل‌جایگزینی با یکدیگر نیستند. DFlash، Medusa و EAGLE را به مدل تصمیم‌گیری تک‌مرحله‌ای که توکن تولید نمی‌کند، مستقیماً نسبت ندهید. انطباق احتمالی آن‌ها با تصمیم‌های چندفیلدی یک فرضیهٔ جداگانه است.

## مسیر استفاده

ابتدا یک شکست واقعی را در مدل پایه پیدا کنید. سپس از این بانک یک مداخله انتخاب کنید، پیشینهٔ نزدیک را کامل بخوانید، یک baseline ساده و معیار ابطال تعریف کنید و فقط پس از آن آزمایش را ثبت کنید. از ترکیب هم‌زمان چندین تکنیک بدون ablation پرهیز کنید. هیچ رتبهٔ SOTA، درصد موفقیت مقاله یا تضمین بهبود در این بانک ساخته نشده است.

ثبت روش تازه: شناسهٔ بعدی را بگیرید، مقالهٔ اولیه را بررسی کنید، کاربرد اصلی را از انتقال پیشنهادی جدا بنویسید و شمارش خانواده و این صفحه را به‌روزرسانی کنید. مدخل ناموفق حذف نمی‌شود؛ نتیجه و دلیل رد به آن افزوده می‌شود.

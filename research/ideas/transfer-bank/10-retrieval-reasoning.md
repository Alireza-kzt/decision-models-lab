# 10 — بازیابی، استدلال و کنترل جریان

[راهنما](README.md). این روش‌ها گاهی بیرون از خود شبکه اجرا می‌شوند. هزینهٔ retrieval، تولید متن و ابزار باید همراه هزینهٔ تصمیم گزارش شود. انتقال‌ها **آزمایش‌نشده** هستند.

## T081 — RAG

**اصل و منبع:** ترکیب بازیابی اسناد با مدل؛ [Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401).

**انتقال و آزمون:** ارائهٔ شواهد بازیابی‌شده به decision encoder، بدون الزام تولید متن؛ no-retrieval، random retrieval و oracle retrieval کنترل‌های مفید هستند.

**پیش‌نیاز و ریسک:** index مجاز و ورودی قابل کنترل؛ corpus نباید پاسخ test را لو بدهد. شواهد نامرتبط یا متناقض ممکن است confidence غلط را بالا ببرند.

## T082 — RETRO

**اصل و منبع:** ادغام بازیابی در معماری مدل؛ [Improving language models by retrieving from trillions of tokens](https://arxiv.org/abs/2112.04426).

**انتقال و آزمون:** cross-attention به chunkهای بازیابی‌شده در encoder تصمیم؛ با concatenation ساده و مدل بدون retrieval مقایسه شود.

**پیش‌نیاز و ریسک:** W/F و index؛ تغییر معماری و آموزش لازم است. هزینهٔ ساخت و به‌روزرسانی index را پنهان نکنیم.

## T083 — kNN augmentation

**اصل و منبع:** ترکیب احتمال مدل با همسایه‌های embedding؛ [Generalization through Memorization: Nearest Neighbor Language Models](https://arxiv.org/abs/1911.00172).

**انتقال و آزمون:** حافظهٔ تصمیم‌های train و ترکیب توزیع همسایه‌ها با head؛ با kNN خالص و مدل پارامتری خالص مقایسه شود.

**پیش‌نیاز و ریسک:** F/P؛ memory باید فقط از دادهٔ مجاز ساخته شود. label index محلی schemaهای متفاوت قابل تجمیع مستقیم نیست.

## T084 — ReAct

**اصل و منبع:** درهم‌آمیختن استدلال و اقدام به ابزار؛ [ReAct](https://arxiv.org/abs/2210.03629).

**انتقال و آزمون:** decision model برای انتخاب ابزار یا توقف؛ با router rule-based و policy بدون متن استدلال مقایسه شود.

**پیش‌نیاز و ریسک:** R و محیط sandbox؛ فراخوانی ابزار اثر خارجی دارد. trace زبانی دلیل کافی برای درست بودن اقدام نیست.

## T085 — Tree of Thoughts

**اصل و منبع:** کاوش چند مسیر حل با ارزیابی میانی؛ [Tree of Thoughts](https://arxiv.org/abs/2305.10601).

**انتقال و آزمون:** مدل تصمیم به‌عنوان evaluator شاخه‌ها؛ با beam search، greedy و scorer ساده در تعداد node برابر مقایسه شود.

**پیش‌نیاز و ریسک:** R و generator/transition معتبر؛ evaluator می‌تواند همان سوگیری مولد را تکرار کند. هزینهٔ کل درخت مهم است.

## T086 — Chain-of-thought prompting

**اصل و منبع:** نمونه‌دادن زنجیرهٔ استدلال برای مدل مولد؛ [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903).

**انتقال و آزمون:** baseline مولدِ پاسخ مستقیم در برابر reasoning-then-decision؛ یک طرح جدا برای distillation این معلم به decision model بدون متن.

**پیش‌نیاز و ریسک:** مدل مولد؛ classifier غیرمولد CoT متنی تولید نمی‌کند. متن توضیح، تضمین وفاداری به محاسبهٔ داخلی نیست.

## T087 — Self-consistency

**اصل و منبع:** تجمیع پاسخ مسیرهای استدلال نمونه‌گیری‌شده؛ [Self-Consistency Improves Chain of Thought Reasoning](https://arxiv.org/abs/2203.11171).

**انتقال و آزمون:** رأی یا توزیع چند نمونهٔ مولد در برابر یک خروجی؛ بودجهٔ token و تعداد فراخوانی ثابت، و اختلاف با ensemble واقعی بررسی شود.

**پیش‌نیاز و ریسک:** نمونه‌گیری متنوع؛ تکرار forward قطعی تنوع ایجاد نمی‌کند. رأی اکثریت ضمانت calibration نیست.

## T088 — DSPy / Program optimization

**اصل و منبع:** بهینه‌سازی برنامه‌های چندمرحله‌ای مبتنی بر مدل؛ [DSPy](https://arxiv.org/abs/2310.03714).

**انتقال و آزمون:** تنظیم prompt، retrieval و تصمیم به‌صورت pipeline؛ ابتدا هر جزء جدا، سپس ترکیب با budget جست‌وجوی ثبت‌شده بررسی شود.

**پیش‌نیاز و ریسک:** دادهٔ dev و کنترل pipeline؛ tuning روی test یا نگه‌داشتن فقط بهترین trial نتیجه را خوش‌بینانه می‌کند. ابزار به‌تنهایی نوآوری پژوهشی نیست.

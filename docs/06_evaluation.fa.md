# پروتکل ارزیابی

## سؤال قبل از metric
مثلاً «آیا بعد از تغییر تعداد گزینه‌ها، افزایش coverage در ریسک ثابت حفظ می‌شود؟» با «مدل کدام است؟» فرق دارد. task، فضای پاسخ، metric اصلی، واحد استقلال، سقف هزینه و آستانهٔ بهبود عملی را قبل از مشاهدهٔ test تعیین کنید.

## جداسازی داده
چهار بخش جدا: train برای وزن؛ dev برای انتخاب روش و hyperparameter؛ calibration برای دما/آستانه؛ test برای گزارش نهایی. خانوادهٔ سؤال، سند، کاربر، ترجمه، paraphrase و همهٔ permutationهای یک نمونه باید در یک group بمانند. split تصادفی ردیف‌ها می‌تواند نشت ایجاد کند.

## تعریف metricهای موجود در runner
برای N نمونهٔ choice با مجموعهٔ ثابت K گزینه در هر مجموعهٔ ارزیابی:

\[
\mathrm{NLL}=-\frac1N\sum_i\log\max(p_{i,y_i},10^{-15}),
\]
\[
\mathrm{Brier}=\frac1N\sum_i\sum_{k=1}^{K}(p_{ik}-\mathbb{1}[y_i=k])^2.
\]

Brier اینجا **جمع روی کلاس‌ها** است، نه میانگین؛ مقدارش را با تعریف متفاوت اشتباه نکنید. clipping در NLL مستند و ثابت است. Accuracy، macro-F1 و ECE top-label با binهای هم‌عرض نیز گزارش می‌شوند؛ ECE به binning حساس است و به‌تنهایی کافی نیست. پیشینهٔ کالیبراسیون: [P005](../catalog/papers/P005.md).

## پذیرش و ارجاع
با confidence برابر بیشینهٔ احتمال و آستانهٔ ثابت t:

\[
\mathrm{coverage}(t)=\frac{\#\{i:c_i\geq t\}}{N},\qquad
\mathrm{risk}(t)=1-\mathrm{accuracy}_{\{i:c_i\geq t\}}.
\]

وقتی هیچ نمونه پذیرفته نشود، risk برابر null است، نه صفر. threshold ثابت روی test گزارش می‌شود؛ انتخاب threshold بر اساس test مجاز نیست. runner فعلی آستانه را optimize نمی‌کند. روش conformal به فرض‌های جدا نیاز دارد؛ [P006](../catalog/papers/P006.md).

## مقایسهٔ منصفانه
task و داده یکی؛ promptها از لحاظ معنا یکسان؛ token budget و context ثبت‌شده؛ نسخهٔ مدل ثابت؛ مقایسهٔ hosted از same-GPU جدا؛ warmup، batch، concurrency، نرخ خطا و cache ثبت شوند. latency درخواست، latency هر تصمیم و throughput یکسان نیستند. معیار صحیح هزینه، هزینهٔ هر تصمیم درست/پذیرفته‌شده نیز هست، نه فقط دلار بر token.

## uncertainty و آزمون آماری
برای آزمایش واقعی چند seed مستقل و paired bootstrap روی groupها لازم است. اندازهٔ نمونهٔ bootstrap، بازهٔ اطمینان، effect size و همهٔ مقایسه‌های اجراشده ثبت شوند. runner اولیه هنوز CI آماری، bootstrap، OOD metric و latency benchmark واقعی ندارد؛ نتیجهٔ آن برای ادعای مقاله کافی نیست.

## مرز پیاده‌سازی
runner در هر evaluation به label universe ثابت نیاز دارد؛ benchmarkهای candidate-variable باید به taskهای همگن بخش‌بندی و سپس با وزن‌های preregistered جمع شوند. multi-label، score ترتیبی و action search هنوز پشتیبانی اجرایی ندارند.

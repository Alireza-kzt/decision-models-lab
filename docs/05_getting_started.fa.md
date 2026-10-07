# راه‌اندازی و استفاده

## محیط پایه
Python 3.11 یا جدیدتر کافی است. هسته فقط از کتابخانهٔ استاندارد استفاده می‌کند؛ GPU، دانلود مدل، pip install و کلید API لازم ندارد. از ریشهٔ پروژه اجرا کنید.

```bash
python -m unittest discover -s tests -v
python -m decision_lab validate
python -m decision_lab smoke --out runs/smoke-001
```

هر پوشهٔ run باید جدید باشد. manifest شامل نوع run، شناسهٔ مدل، revision، hash داده و ورودی احتمالات، محیط، وضعیت Git و زمان UTC است. پوشه‌های runs در Git نادیده گرفته می‌شوند. گزارش منتخب و بی‌خطر را پس از بازبینی به reports منتقل کنید.

## ارزیابی خروجی ذخیره‌شده
JSONL داده شامل id، state، question، options، label، group_id و split است. JSONL پیش‌بینی شامل id و probabilities با دقیقاً همان کلیدهای options است. ادغام با id انجام می‌شود، نه شمارهٔ ردیف. شناسهٔ اضافه، تکراری، گمشده، NaN یا احتمال نامعتبر خطا می‌دهد؛ تعمیر خاموش نداریم.

```bash
python -m decision_lab evaluate --dataset data/examples/toy.jsonl --predictions data/examples/replay.jsonl --out runs/replay-001 --kind demonstration --model-id hand-authored-fixture --revision fixture-v1
```

این مثال داده و احتمال دست‌نویس دارد و نتیجهٔ مدل نیست. برای دادهٔ واقعی `--kind research` و شناسهٔ واقعی مدل، revision و split همگن لازم است؛ تنظیم metricها باید در پروتکل ثبت شود.

## افزودن مدل واقعی
از [راهنمای adapter](10_adapter_contract.fa.md) پیروی کنید. اولین integration را با fixture و raw response ذخیره‌شده شروع کنید. live adapter هنوز در این تحویل وجود ندارد. نصب upstream و download وزن را جداگانه، با نسخهٔ قفل‌شده و مجوز روشن انجام دهید.

## روی ویندوز
همین دستورهای Python در PowerShell قابل اجرا هستند. برای ساخت ریپوی private، ابزار `gh` باید روی دستگاه خودتان نصب و authenticated باشد؛ [وضعیت تحویل](../DELIVERY.md) را ببینید. هیچ توکنی در فایل‌های این بسته قرار نمی‌گیرد.

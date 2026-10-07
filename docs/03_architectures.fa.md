# مطالعهٔ معماری و نقاط تغییر

این بخش یک زبان مشترک برای تحلیل است. کارت هر مدل مشخص می‌کند کدام جزئیات گزارش شده و کدام مجهول‌اند.

## خانوادهٔ A: encoder و head شرطی به schema
متن/ساختار state و تعریف گزینه‌ها encode می‌شوند؛ head به هر گزینه امتیاز می‌دهد. شکل کلی:

\[
z_i=g_\phi(h_s,h_q,h_{a_i},H_A),\qquad p_i=\operatorname{softmax}_i(z).
\]

head ثابتِ کلاس‌ها با head شرطی به candidate متفاوت است. اولی برای برچسب‌های ثابت ساده‌تر است؛ دومی باید معنای گزینهٔ تازه را بفهمد. برای مطالعهٔ نمونهٔ کوچک به کارت GLiNER و Laya مراجعه کنید، نه اینکه این فرمول را توصیف دقیق آن‌ها فرض کنید.

## خانوادهٔ B: backbone زبانی و امتیازدهی مستقیم
representationهای یک backbone برای امتیاز گزینه‌ها استفاده می‌شوند؛ هیچ متن آزاد لازم نیست. محورهای تغییر: توجه یک‌طرفه/دوطرفه/بلوک‌بندی، pooling، pointer head، cross-attention، به‌اشتراک‌گذاری state، گزینه‌های variable-cardinality، و سربار schema. جزئیات گزارش‌شدهٔ Clef و Kev در کارت‌هایشان آمده است.

## خانوادهٔ C: baseline مولد محدودشده
مدل، یک شناسه/حرف/JSON مجاز تولید می‌کند یا likelihood شناسه‌ها خوانده می‌شود. این baseline را حذف نکنید: برای فهمیدن سهم آموزش تصمیمی لازم است. احتمال شناسه‌های چندتوکنی باید با سیاست مشخص محاسبه شود؛ مقایسهٔ یک حرف با جملهٔ چندتوکنی خام منصفانه نیست. Tev1 در این گروه ثبت شده است.

## خانوادهٔ D: سرویس بسته
API قرارداد خروجی را می‌دهد، نه همهٔ معماری را. برای سرویس بسته فقط فرضیهٔ رفتاری آزمایش می‌کنیم و مدل پایه/تعداد لایه/روش exact آموزش را حدس نمی‌زنیم.

## ماتریس تغییر قابل مطالعه
| مؤلفه | کنترل ضروری | خطر تفسیر |
|---|---|---|
| حذف causal mask | همان داده و optimizer | نسبت‌دادن اثر داده به معماری |
| head مشترک چند سؤال | head مستقل با بودجهٔ مشابه | تداخل سؤال‌ها یا نشت label |
| loss کالیبراسیون | CE، دمای post-hoc، CE+Brier | تنظیم calibration روی test |
| ناوردایی گزینه‌ها | augmentation و ensemble ساده | ادعای novelty برای روش موجود |
| distillation | student بدون teacher و با همان داده | نشت benchmark از teacher |
| policy/value | heuristic و policy-only | نسبت‌دادن اثر solver به مدل |

## چک‌لیست code audit پیش از اصلاح
در یک branch جدا، commit upstream را pin کنید؛ tokenizer/config/attention mask/head/loss/data builder را پیدا کنید؛ shapes را با fixture ثبت کنید؛ پارامترهای trainable را بشمارید؛ forward pass و گرادیان یک batch را تست کنید؛ license فایل‌های کد و وزن را جدا بخوانید. اجرای کد ناشناس با trust_remote_code بدون ممیزی ممنوع است.

لینک‌های پایه: [فهرست مدل‌ها](../catalog/README.md)، [Kev](../catalog/models/kev.md)، [Clef](../catalog/models/clef.md)، [Tev1](../catalog/models/tev1.md).

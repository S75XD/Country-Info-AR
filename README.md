# سكربت معلومات الدول

هذا السكربت في بايثون يوفر دالة للحصول على اسم الدولة الكامل والإيموجي الخاص بها بناءً على رمز الدولة المكون من حرفين وفقًا لنظام ISO 3166-1 alpha-2. أسماء الدول موفرة باللغة العربية مع الأعلام الخاصة بها.

## كيفية الاستخدام

1. قم باستنساخ أو تنزيل هذا المستودع.
2. قم بتشغيل السكربت `country_info.py`.

### مثال

```python
def get_country_info(country_code):
    # تحويل الاختصار إلى حروف كبيرة للتأكد من التوافق
    country_code = country_code.upper()
    if country_code in countries:
        return countries[country_code]
    else:
        return "Country code not found"

# اختبار الدالة
print(get_country_info("SA"))  # ("المملكة العربية السعودية", "🇸🇦")
print(get_country_info("US"))  # ("الولايات المتحدة الأمريكية", "🇺🇸")
print(get_country_info("CN"))  # ("الصين", "🇨🇳")
print(get_country_info("XYZ")) # "Country code not found"
```

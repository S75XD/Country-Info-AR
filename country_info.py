countries = {
    "SA": ("المملكة العربية السعودية", "🇸🇦"),
    "US": ("الولايات المتحدة الأمريكية", "🇺🇸"),
    "CA": ("كندا", "🇨🇦"),
    "FR": ("فرنسا", "🇫🇷"),
    "DE": ("ألمانيا", "🇩🇪"),
    "IT": ("إيطاليا", "🇮🇹"),
    "ES": ("إسبانيا", "🇪🇸"),
    "GB": ("المملكة المتحدة", "🇬🇧"),
    "CN": ("الصين", "🇨🇳"),
    "JP": ("اليابان", "🇯🇵"),
    "AE": ("الإمارات العربية المتحدة", "🇦🇪"),
    "AU": ("أستراليا", "🇦🇺"),
    "BR": ("البرازيل", "🇧🇷"),
    "IN": ("الهند", "🇮🇳"),
    "RU": ("روسيا", "🇷🇺"),
    "ZA": ("جنوب أفريقيا", "🇿🇦"),
    "MX": ("المكسيك", "🇲🇽"),
    "KR": ("كوريا الجنوبية", "🇰🇷"),
    "AR": ("الأرجنتين", "🇦🇷"),
    "SE": ("السويد", "🇸🇪"),
    "CH": ("سويسرا", "🇨🇭"),
    "NL": ("هولندا", "🇳🇱"),
    "TR": ("تركيا", "🇹🇷"),
    "EG": ("مصر", "🇪🇬"),
    "NG": ("نيجيريا", "🇳🇬"),
    "PK": ("باكستان", "🇵🇰"),
    "ID": ("إندونيسيا", "🇮🇩"),
    "TH": ("تايلاند", "🇹🇭"),
    "SG": ("سنغافورة", "🇸🇬"),
    "MY": ("ماليزيا", "🇲🇾"),
    "PH": ("الفلبين", "🇵🇭"),
    "VN": ("فيتنام", "🇻🇳"),
    "NO": ("النرويج", "🇳🇴"),
    "DK": ("الدنمارك", "🇩🇰"),
    "FI": ("فنلندا", "🇫🇮"),
    "PL": ("بولندا", "🇵🇱"),
    "GR": ("اليونان", "🇬🇷"),
    "PT": ("البرتغال", "🇵🇹"),
    "HU": ("المجر", "🇭🇺"),
    "AT": ("النمسا", "🇦🇹"),
    "BE": ("بلجيكا", "🇧🇪"),
    "IE": ("أيرلندا", "🇮🇪"),
    "IL": ("إسرائيل", "🇮🇱"),
    "NZ": ("نيوزيلندا", "🇳🇿"),
    "UA": ("أوكرانيا", "🇺🇦"),
    "KE": ("كينيا", "🇰🇪"),
    "GH": ("غانا", "🇬🇭"),
    "DZ": ("الجزائر", "🇩🇿"),
    "MA": ("المغرب", "🇲🇦"),
    "LY": ("ليبيا", "🇱🇾"),
    "QA": ("قطر", "🇶🇦"),
    "KW": ("الكويت", "🇰🇼"),
    "BH": ("البحرين", "🇧ahr🇮"),
    "OM": ("عمان", "🇴🇲"),
    "JO": ("الأردن", "🇯🇴"),
    "LB": ("لبنان", "🇱🇧"),
    "IQ": ("العراق", "🇮🇶"),
    "SY": ("سوريا", "🇸🇾"),
    "YE": ("اليمن", "🇾🇪"),
    "SD": ("السودان", "🇸🇩"),
    "TN": ("تونس", "🇹🇳"),
    "SN": ("السنغال", "🇸🇳"),
    "UG": ("أوغندا", "🇺🇬"),
    "TZ": ("تنزانيا", "🇹🇿"),
    "ZM": ("زامبيا", "🇿🇲"),
    "ZW": ("زيمبابوي", "🇿🇼"),
    "BG": ("بلغاريا", "🇧🇬"),
    "RO": ("رومانيا", "🇷🇴"),
    "HR": ("كرواتيا", "🇭🇷"),
    "CZ": ("جمهورية التشيك", "🇨🇿"),
    "SK": ("سلوفاكيا", "🇸🇰"),
    "SI": ("سلوفينيا", "🇸🇮"),
    "RS": ("صربيا", "🇷🇸"),
    "BA": ("البوسنة والهرسك", "🇧🇦"),
    "MK": ("مقدونيا الشمالية", "🇲🇰"),
    "ME": ("الجبل الأسود", "🇲🇪"),
    "AL": ("ألبانيا", "🇦🇱"),
    "BY": ("بيلاروسيا", "🇧🇾"),
    "KZ": ("كازاخستان", "🇰🇿"),
    "UZ": ("أوزبكستان", "🇺🇿"),
    "MN": ("منغوليا", "🇲🇳"),
    "BD": ("بنغلاديش", "🇧🇩"),
    "LK": ("سريلانكا", "🇱🇰"),
    "NP": ("نيبال", "🇳🇵"),
    "MM": ("ميانمار", "🇲🇲"),
    "KH": ("كمبوديا", "🇰🇭"),
    "LA": ("لاوس", "🇱🇦"),
    "BT": ("بوتان", "🇧🇹"),
    "MV": ("جزر المالديف", "🇲🇻"),
    "AM": ("أرمينيا", "🇦🇲"),
    "GE": ("جورجيا", "🇬🇪"),
    "AZ": ("أذربيجان", "🇦🇿"),
    "TJ": ("طاجيكستان", "🇹🇯"),
    "TM": ("تركمانستان", "🇹🇲"),
    "KG": ("قيرغيزستان", "🇰🇬"),
}

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

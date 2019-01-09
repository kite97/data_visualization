# coding=gbk

from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """����ָ���Ĺ��ң�����Pygalʹ�õ�������ĸ�Ĺ�����"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # ���û���ҵ�ָ���Ĺ��ң��ͷ���None
    return None

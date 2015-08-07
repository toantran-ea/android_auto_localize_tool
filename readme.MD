## Translate strings.xml resources to different localizations.

## Usage:
1. Place your strings.xml in same directory of `localize_tool.py`
2. Run 
   ```python localize_tool.py  <target_language_code>```
3. Check the output result: `translated_strings.xml` for resources that can be automagically translated and `untranslated_strings.xml` for resources that can not be decoded to translate.
4. Enjoy!

## Background stack:
 - Auto-translate tool powered by [Goslate](https://pypi.python.org/pypi/goslate)
 - Run `./update.sh` to update `Goslate` tool.


## Example: 
```
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="invisible_in_main_device_list">撤销我的设备列表显示</string>
    <string name="yeelight_name">Yeelight床头灯</string>
    <string name="router_test_testing">正在检测小米路由器</string>
    <string name="router_test_info">使用小米路由器连接%s</string>
    <string name="router_test_sub_info">路由器名称：%s</string>
    <string name="router_test_switch">切换网络</string>
    <string name="dialog_title_create_yeelight_group">Yeelight智能灯可创建灯组统一管理</string>
    <string name="dialog_button_create_yeelight_group">创建灯组</string>
    <string name="activity_title_modify_group">Yeelight灯组</string>
    <string name="yeelight_default_group">Yeelight灯组</string>
    <string name="group_device">创建Yeelight灯组</string>
    <string name="toast_create_group_success">创建分组成功</string>
    <string name="toast_create_group_failed">创建分组失败</string>
    <string name="smarthome_device_virtual_delete">删除分组</string>
    <string name="visible_in_main_device_list_success">添加成功</string>
    <string name="invisible_in_main_device_list_success">撤销成功</string>
    <string name="visible_in_main_device_list_failed">添加失败</string>
    <string name="invisible_in_main_device_list_failed">撤销失败</string>
    <string name="yeelight_color_preset0">白色</string>
    <string name="yeelight_color_preset1">浪漫</string>
    <string name="yeelight_color_preset2">黄色</string>
    <string name="yeelight_color_preset3">迷情</string>
    <string name="yeelight_hint_enter_color_name">请输入自定义名称</string>
    <string name="yeelight_toast_name_too_long">名称不能多于4个中文字符</string>
    <string name="yeelight_btn_save">保存</string>
    <string name="yeelight_bright_value">亮度：</string>
    <string name="yeelight_color_value">色值：</string>
    <string name="yeelight_color_desc0">白色：代表纯洁，象征着圣洁优雅。无比的高洁、明亮，在森罗万象中有其高远的意境。白色寓意着公正、纯洁、端庄、正直、少壮、超脱凡尘与世俗的情感。</string>
    <string name="yeelight_color_desc1">浪漫：粉红色：粉红色代表可爱浪漫、富有幻想色彩。小女生比较会沉静在自己营造童话王国内幻想着自己的王子、自己的爱情、自己的美好的一切。</string>
    <string name="yeelight_color_desc2">黄色：黄色给人一种心平静的感觉， 让人眼睛清澈明亮； 黄色还给人一种对美好生活的向往。黄色的灿烂、辉煌，有着太阳般的光辉，象征着照亮黑暗的智慧之光。</string>
    <string name="yeelight_color_desc3">迷情：紫色：代表一种强烈的感情，喜欢紫色的人的性格优雅而高尚，具有丰富的感受性，细腻而敏感，审美趣味高雅，对此自我也很明白。</string>
    <string name="yeelight_btn_txt_back">返回</string>
    <string name="yeelight_btn_txt_del">删除</string>
    <string name="yeelight_btn_txt_ok">确定</string>
</resources>
```
 ``` python localize_tool.py en```
 
 Result: `translated_strings.xml`
 ```
 <?xml version='1.0' encoding='utf-8'?>
<resources>
   <string name="invisible_in_main_device_list">Undo my list of devices display</string>
   <string name="yeelight_name">Yeelight bedside lamp</string>
   <string name="router_test_testing">Detecting millet router</string>
   <string name="router_test_info">Use millet router% s</string>
   <string name="router_test_sub_info">Router Name:% s</string>
   <string name="router_test_switch">Switching Network</string>
   <string name="dialog_title_create_yeelight_group">Yeelight intelligent lights can create a light set of unified management</string>
   <string name="dialog_button_create_yeelight_group">Create lamps</string>
   <string name="activity_title_modify_group">Yeelight lamps</string>
   <string name="yeelight_default_group">Yeelight lamps</string>
   <string name="group_device">Create Yeelight lamps</string>
   <string name="toast_create_group_success">Create a packet success</string>
   <string name="toast_create_group_failed">Create a packet fails</string>
   <string name="smarthome_device_virtual_delete">Delete Group</string>
   <string name="visible_in_main_device_list_success">Added successfully</string>
   <string name="invisible_in_main_device_list_success">Revocation of success</string>
   <string name="visible_in_main_device_list_failed">Add Failed</string>
   <string name="invisible_in_main_device_list_failed">Revocation failure</string>
   <string name="yeelight_color_preset0">White</string>
   <string name="yeelight_color_preset1">Romantic</string>
   <string name="yeelight_color_preset2">Yellow</string>
   <string name="yeelight_color_preset3">Sensation</string>
   <string name="yeelight_hint_enter_color_name">Please enter a custom name</string>
   <string name="yeelight_toast_name_too_long">Name can not be more than four Chinese characters</string>
   <string name="yeelight_btn_save">Save</string>
   <string name="yeelight_bright_value">Brightness:</string>
   <string name="yeelight_color_value">Color values:</string>
   <string name="yeelight_color_desc0">White: represents purity, symbolizes holiness elegance. Very noble, bright, lofty mood in its flowers will Vientiane. White symbolizes the fair, pure, dignified, upright, young and vigorous, detached mundane and worldly emotions.</string>
   <string name="yeelight_color_desc1">Romance: Pink: Pink is lovely and romantic, fanciful colors. Little girls more likely to create their own fairy tale steeped in the fantasy kingdom of their prince, their love, their own good everything.</string>
   <string name="yeelight_color_desc2">Yellow: Yellow gives a feeling of calm mind, let the eyes clear and bright; yellow gave people a better life for himself. Yellow brilliant, brilliant, with a sun-like brilliance, symbolizing the light of wisdom to illuminate the darkness.</string>
   <string name="yeelight_color_desc3">Sensation: Purple: represents a strong emotion, like purple elegant and noble personality, has a wealth of sensitivity, delicate and sensitive, aesthetic taste and elegant, this is also very self-aware.</string>
   <string name="yeelight_btn_txt_back">Return</string>
   <string name="yeelight_btn_txt_del">Delete</string>
   <string name="yeelight_btn_txt_ok">Determine</string>
</resources>
 ```
 
## Check supported languages here:
[https://cloud.google.com/translate/v2/using_rest#target](https://cloud.google.com/translate/v2/using_rest#target)